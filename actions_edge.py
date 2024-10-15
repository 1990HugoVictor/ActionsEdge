"""
This program opens the Task View when the mouse moves to the upper-left corner of the screen.

Zero Clause BSD License

Copyright (c) 2024, Victor Hugo

Permission to use, copy, modify, and distribute this software for
any purpose with or without fee is hereby granted.
"""

import ctypes
import sys
import threading
import time
from typing import Tuple


# Constants for the mouse position threshold and the key codes
THRESHOLD = 0.05  # Fraction of screen size for mouse movement detection
MOVEMENT_TIME = 0.5  # Time in seconds to detect if mouse is at (0, 0)
SLEEP_INTERVAL = 0.1  # Sleep time between mouse position checks in seconds
WINDOWS_KEY = 0x5B  # Virtual key code for Windows key
TAB_KEY = 0x09  # Virtual key code for Tab key


class Point(ctypes.Structure):
    """Represents a point in a two-dimensional space."""
    _fields_ = [("x", ctypes.c_long), ("y", ctypes.c_long)]

    def __init__(self, x: int = 0, y: int = 0) -> None:
        """Initialize the Point with optional coordinates."""
        self.x = x
        self.y = y

    def __str__(self) -> str:
        """Return a string representation of the point."""
        return f"Point(x={self.x}, y={self.y})"

    def set_position(self, x: int, y: int) -> None:
        """Set the x and y coordinates of the point."""
        self.x = x
        self.y = y


def get_mouse_position() -> Tuple[int, int]:
    """Capture the current mouse position.

    Returns:
        Tuple[int, int]: A tuple containing the x and y coordinates of the mouse.
    """
    point = Point()  # Create a new Point object
    ctypes.windll.user32.GetCursorPos(ctypes.byref(point))
    return point.x, point.y


def is_admin() -> bool:
    """Check if the script is running with administrator privileges.

    Returns:
        bool: True if running as admin, False otherwise.
    """
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except OSError:
        print("Error checking admin status")
        return False


def run_task_view() -> None:
    """Simulate opening Task View."""
    ctypes.windll.user32.keybd_event(WINDOWS_KEY, 0, 0, 0)  # Press Windows key
    ctypes.windll.user32.keybd_event(TAB_KEY, 0, 0, 0)  # Press Tab key
    ctypes.windll.user32.keybd_event(TAB_KEY, 0, 2, 0)  # Release Tab key
    ctypes.windll.user32.keybd_event(WINDOWS_KEY, 0, 2, 0)  # Release Windows key


def monitor_mouse(last_movement_time: float, lock: threading.Lock) -> None:
    """Monitor the mouse position and trigger Task View if needed.

    Args:
        last_movement_time (float): The last time the mouse was moved.
        lock (threading.Lock): A lock to synchronize access to shared resources.
    """
    screen_width = ctypes.windll.user32.GetSystemMetrics(0)
    screen_height = ctypes.windll.user32.GetSystemMetrics(1)
    is_task_view_opened = False

    while True:
        x, y = get_mouse_position()

        # Check if the mouse moved out of the top-left corner
        if x >= screen_width * THRESHOLD and y >= screen_height * THRESHOLD:
            last_movement_time = time.time()

        # If the mouse is in the corner and within the time limit, open Task View
        with lock:
            mouse_in_corner = (x <= 0 and y <= 0)
            if (time.time() < last_movement_time + MOVEMENT_TIME) and mouse_in_corner:
                if not is_task_view_opened:
                    threading.Thread(target=run_task_view).start()
                    is_task_view_opened = True
            else:
                is_task_view_opened = False

        time.sleep(SLEEP_INTERVAL)  # Wait for the defined sleep interval


def elevate_privileges() -> None:
    """Restart the script with elevated privileges if not already running as admin."""
    ctypes.windll.shell32.ShellExecuteW(
        None, "runas", sys.executable,
        " ".join(sys.argv), None, 1
    )
    sys.exit()


def main() -> None:
    """Main function to execute the script."""
    if not is_admin():
        elevate_privileges()

    last_movement_time = time.time()
    lock = threading.Lock()  # Create a lock for thread safety

    # Start monitoring the mouse
    monitor_mouse(last_movement_time, lock)


if __name__ == "__main__":
    main()
