#Import modules
import os
import tkinter as tk
import ttkbootstrap as ttk
import pyautogui
import time

#Change the working directory to the file's location
os.chdir(os.path.dirname(__file__))


#Create the window
root = ttk.Window()
#Sets the window's geometry
try:
    with open("lastGeometry.txt", 'r') as f:
        lastGeometry = f.read()

    screenResolution = pyautogui.size()
    screenWidth = screenResolution[0]
    screenHeight = screenResolution[1]
    defaultWidth = int(screenWidth / 2)
    defaultHeight = int(screenHeight / 2)

    if lastGeometry == "":
        print("First launch, opening in the default resolution")
        startResolution = f"{defaultWidth}x{defaultHeight}"
        root.geometry(f"{defaultWidth}x{defaultHeight}")
    else:
        print("Attempting to open in the last resolution")
        try:
            root.geometry(lastGeometry)
            print(f"Successfuly opened in the last resolution: {lastGeometry}")
            startResolution = lastGeometry
        except:
            print("Error: lastGeometry.txt's text is corrupted, opening in the default resolution and clearing the file")
            with open("lastGeometry.txt", 'w') as f:
                f.write("")
            startResolution = f"{defaultWidth}x{defaultHeight}"
            root.geometry(f"{defaultWidth}x{defaultHeight}")
except:
    print("Error: lastGeometry.txt does not exist, program launched in the default resolution and lastGeometry.txt created")
    os.system("touch lastGeometry.txt")
    root.geometry(f"{defaultWidth}x{defaultHeight}")

#Sets the window's position
try:
    with open("lastPosition.txt", 'r') as f:
        lastPosition = f.read()

    if lastPosition == "":
        print("First launch, opening in the default position")
        time.sleep(0.1)
        root.position_center()
    else:
        print("Attempting to open in the last position")
        try:
            root.geometry(f"{startResolution}+{lastPosition}")
            print(f"Successfuly opened in the last position: {lastPosition}")
        except:
            print("Error: lastPositions.txt's text is corrupted, opening in default resolution and clearing the file")
            with open("lastPosition.txt", 'w') as f:
                f.write("")
            time.sleep(0.1)
            root.position_center()
except:
    print("Error: lastPosition.txt does not exist, program launched and lastGeometry.txt created")
    os.system("touch lastPosition.txt")
    time.sleep(0.1)
    root.position_center()

#A function that saves the resolution and position
def onClosing():
    with open("lastGeometry.txt", 'w') as f:
       f.write(f"{root.winfo_width()}x{root.winfo_height()}")
    print("Resolution saved successfuly")
    with open("lastPosition.txt", 'w') as f:
        f.write(f"{root.winfo_x()}+{root.winfo_y()}")
    print("Position saved succesfuly")
    root.quit()


#A function that gets the users home directory
def getHomeDirectory():
    user = os.popen("whoami")
    return f"/home/{user.read().strip()}"

homeDirectory = getHomeDirectory()

#Function listing all files in a directory 
def getFilesInDirectory(dir):
    filesStream = os.popen(f"ls -1 {dir}")
    stringOfFilesInDirectory = filesStream.read().strip()
    return stringOfFilesInDirectory.splitlines()

#Fire the onClosing function when the window is closed
root.protocol("WM_DELETE_WINDOW", onClosing)

#Start the application mainloop
root.mainloop()

