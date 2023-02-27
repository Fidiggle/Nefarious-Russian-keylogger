This is a simple python program that's supposed to run as a background process, and it's meant for quickly
launching batch files.

These files are launched by typing the name of the batch file and then pressing the print screen button.

The program is currently used only to launch neg.bat, which copies a long list of generic negative prompts
used in stable diffusion onto the clipboard, and pho.bat, which launches photoshop on my computer.

To add shortcuts to batch files, you currently need to edit "Nefarious Russian keylogger.py" itself, but 
meta programming could be added to automatically create a command for each bat file in the main directory.