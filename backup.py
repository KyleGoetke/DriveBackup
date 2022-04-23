# Created by Kyle Goetke
# v0.3 - April 22, 2022

import win32api
import time
from datetime import datetime
import subprocess
import sys
import os

print("--------")
print("E:\\ not located. Waiting for drive.")
print("--------")
while True:
    time.sleep(3)
    drive_list = win32api.GetLogicalDriveStrings()
    drive_list = drive_list.split("\x00")[0:-1]  # the last element is ""
    print("Checking drives:")
    time.sleep(1)
    for letter in drive_list:
        drive = "{0}".format(letter)
        if drive != "E:\\":
            print(" ", drive)
            time.sleep(1)
            continue
        elif drive == "E:\\":
            print(" ", drive)
            time.sleep(0.25)
            user_check = input(f"\nDo you want to copy from {drive} (Y/N)?\n> ").upper()
            if user_check[0] == "Y":
                src_path = f"{drive}"
                now = datetime.now()
                # current_time = now.strftime("%b_%d_%Y_%H_%M") # 24 hr time
                current_time = now.strftime("%b_%d_%Y_%I_%M_%p") # 12 hr time
                custom_path = input("\nWould you like to name the destination folder (Y/N)?\n> ").upper()
                if custom_path[0] == "Y":
                    custom_path = input("\nEnter folder name:\n> ")
                    dest_path = f"D:\\{custom_path}_{current_time}\\"
                else:
                    dest_path = f"D:\\NEW_BACKUP_{current_time}\\"
                try:
                    robocopy_output = subprocess.call(f"robocopy {src_path} {dest_path} /E /V /COPYALL /DCOPY:DAT /R:10 /W:5", shell=True)
                    if robocopy_output != 1:
                        print("\nError encountered:", robocopy_output, file=sys.stderr)
                        print("")
                    else:
                        print("Robocopy returned:", robocopy_output, file=sys.stderr)
                except OSError as e:
                    print("Execution failed:", e, file=sys.stderr)
            else:
                os.system("cls")
                print("\n--------")
                print("E:\\ not located. Waiting for drive.")
                print("--------")
        else:
            print("BIG ISSUE!!!")
            print("Detected drive {drive} caught by else")
    print("All drives checked.")
    time.sleep(1)
    print("Starting new check in 15 seconds.")
    time.sleep(3)
    print("--------")
