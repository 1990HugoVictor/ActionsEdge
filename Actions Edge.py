"""
This module provides functionality to create a scheduled task 
with administrator privileges on Windows using PowerShell. 
It includes functions to check admin status, run scripts as 
an administrator, create scheduled tasks, and modify power 
conditions for those tasks.
"""

import os
import sys
import subprocess
import ctypes


def is_admin():
    """Check if the script is being run with administrator privileges."""
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except (OSError, RuntimeError):
        return False


def run_as_admin():
    """Restart the script as an administrator."""
    if sys.argv[0] == "python.exe":
        # If the script was called directly by Python, get the script's path.
        script_path = os.path.abspath(sys.argv[1])
    else:
        script_path = os.path.abspath(sys.argv[0])

    # Restart the script with administrator privileges
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable, script_path, None, 1
    )


def create_task(task_name, executable_path):
    """Create a scheduled task with the specified parameters using PowerShell."""
    powershell_command = f'''
    $Action = New-ScheduledTaskAction -Execute "{executable_path}"
    $Trigger = New-ScheduledTaskTrigger -AtLogOn
    $Settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries `
    -DontStopIfGoingOnBatteries -StartWhenAvailable
    $Principal = New-ScheduledTaskPrincipal -UserId "SYSTEM" `
    -LogonType ServiceAccount
    Register-ScheduledTask -Action $Action -Trigger $Trigger `
    -Settings $Settings -Principal $Principal -TaskName "{task_name}"
    '''

    try:
        subprocess.run(
            ["powershell", "-Command", powershell_command],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Task '{task_name}' created successfully.")

        # Remove power conditions if they were added
        modify_power_conditions(task_name)

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while creating the task: {e}")
        print(f"Error output: {e.stderr}")


def modify_power_conditions(task_name):
    """Remove power conditions from the task."""
    remove_conditions_command = f'''
    $task = Get-ScheduledTask -TaskName "{task_name}"
    $task.Principal.UserId = "SYSTEM"
    $task.Principal.LogonType = "ServiceAccount"
    $task.Settings.AllowStartIfOnBatteries = $true
    $task.Settings.DontStopIfGoingOnBatteries = $true
    $task.Settings.StartWhenAvailable = $true
    Set-ScheduledTask -TaskName "{task_name}" -InputObject $task
    '''

    try:
        subprocess.run(
            ["powershell", "-Command", remove_conditions_command],
            check=True,
            capture_output=True,
            text=True
        )
        print(f"Power conditions for task '{task_name}' adjusted successfully.")

    except subprocess.CalledProcessError as e:
        print(f"An error occurred while modifying the power conditions of the task: {e}")
        print(f"Error output: {e.stderr}")


if __name__ == "__main__":
    # Task name
    TASK_NAME = "Actions Edge"

    # Absolute path of the executable
    EXECUTABLE_PATH = os.path.join(
        os.path.dirname(os.path.abspath(__file__)),
        "actions_edge.exe"
    )

    # Check if running as admin
    if not is_admin():
        print("Attempting to restart the script as an administrator...")
        run_as_admin()
    else:
        create_task(TASK_NAME, EXECUTABLE_PATH)
