<p align="left">
  <img src="actions_edge.ico" alt="Ícone" width="128" height="128">
</p>

[![Versão](https://img.shields.io/badge/Versão-1.0.0-blue.svg)](https://github.com/seu-usuario/seu-repositorio)
[![GitHub Issues](https://img.shields.io/github/issues/1990HugoVictor/ActionsEdge)](https://github.com/1990HugoVictor/ActionsEdge/issues)
[![License](https://img.shields.io/github/license/1990HugoVictor/ActionsEdge)](./LICENSE)

# Actions Edge  

Actions Edge is a tool that optimizes navigation in Windows by allowing quick access to Task View when the mouse moves to the upper-left corner of the screen. It is designed to enhance workflow efficiency by providing a seamless way to manage open applications and desktops.  

## Features  

- Automatically opens Task View when the mouse moves to the upper-left corner of the screen.  
- Requires administrator privileges to run.  
- Lightweight and runs in the background.  
- **Compatible only with Windows 10 and 11.**  

## Prerequisites  

- **Python 3**: Ensure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).  
- **Libraries**: This project may require additional Python libraries. Please ensure all dependencies are installed.

## Installation  

1. **Clone the repository:**  
   ```bash
   git clone https://github.com/yourusername/actions-edge.git  
   cd actions-edge  
   ```

2. **Install Python:**  
   Make sure you have Python 3 installed on your system. You can download it from [python.org](https://www.python.org/downloads/).  

3. **Run the script:**  
   You may need to run it with administrator privileges.  

   ```bash
   python actions_edge.py  
   ```

## Usage  

- Simply move your mouse to the upper-left corner of the screen (position (0, 0)) to trigger Task View.  
- To stop the program, you should terminate Python in the **Task Manager** or restart your computer.  
- **Example Use Case:** Ideal for users who frequently switch between applications, allowing for quick access to all open windows.

## Code Overview  

- The script monitors the mouse position and checks if it moves from outside the **threshold** to the upper-left corner of the screen for a defined duration (`MOVEMENT_TIME`).  
- If the conditions are met, it simulates the keyboard shortcut to open Task View (using the Windows key and Tab).  
- The code is organized into a class to represent the mouse position, and includes functions to check admin privileges, monitor the mouse, and open Task View.  

## License  

```
Zero-Clause BSD  
===============

Permission to use, copy, modify, and/or distribute this software for  
any purpose with or without fee is hereby granted.  

THE SOFTWARE IS PROVIDED “AS IS” AND THE AUTHOR DISCLAIMS ALL  
WARRANTIES WITH REGARD TO THIS SOFTWARE INCLUDING ALL IMPLIED WARRANTIES  
OF MERCHANTABILITY AND FITNESS. IN NO EVENT SHALL THE AUTHOR BE LIABLE  
FOR ANY SPECIAL, DIRECT, INDIRECT, OR CONSEQUENTIAL DAMAGES OR ANY  
DAMAGES WHATSOEVER RESULTING FROM LOSS OF USE, DATA OR PROFITS, WHETHER IN  
AN ACTION OF CONTRACT, NEGLIGENCE OR OTHER TORTIOUS ACTION, ARISING OUT  
OF OR IN CONNECTION WITH THE USE OR PERFORMANCE OF THIS SOFTWARE.  
```

## Donations  

If you liked the project and want to support it, feel free to contribute:  
**Bitcoin Wallet:**  
`bc1qvcchvz5490m55uz29ulcpvell90dxscwln7qpy`  

## Acknowledgments  

Special thanks to the open-source community for their invaluable resources and support.  
