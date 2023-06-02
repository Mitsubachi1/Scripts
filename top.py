import win32gui
import win32con

# Replace 'Notepad' with the title of the window you want to set always on top
while True:
    hwnd = win32gui.FindWindow(None, 'The Wireshark Network Analyzer')

# Set the window to be always on top
    win32gui.SetWindowPos(hwnd, win32con.HWND_TOPMOST, 0, 0, 0, 0, win32con.SWP_NOMOVE | win32con.SWP_NOSIZE)

# Start the program that you want to set always on top
# This example starts Notepad, but you can replace this with any program you want
while True:
    import subprocess
    subprocess.Popen('C:\Program Files\Wireshark\shark.exe')
