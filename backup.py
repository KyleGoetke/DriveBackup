# Created by Kyle Goetke
# v0.2 - April 20, 2022

import win32api
import win32file
import time
from datetime import datetime, timedelta
import subprocess
import sys

while True:
    time.sleep(3)
    drive_list = win32api.GetLogicalDriveStrings()
    drive_list = drive_list.split("\x00")[0:-1] # the last element is ""
    for letter in drive_list:
        if win32file.GetDriveType(letter) == win32file.DRIVE_REMOVABLE:
            drive = "{0}".format(letter)
            print("\n--------\n")
            user_check = input(f"Do you want to copy from {drive} (Y/N)?\n> ".format(letter)).upper()
            if user_check[0] == "Y":
                src_path = f"{drive}"
                now = datetime.now()
                current_time = now.strftime("%B %d %Y %H.%M.%S")
                dest_path = f"D:\\NEW BACKUP {current_time}"
                print(f"\nBackup will be located in {dest_path}")
                start_time = time.time()
                #! robocopy starts here
                try:
                    robocopy_output = subprocess.call(f"robocopy {src_path} {dest_path} /e /copyall", shell=True)
                    if robocopy_output < 0:
                        print("# Terminated by signal:", -robocopy_output, file=sys.stderr)
                    else:
                        print("# Returned:", robocopy_output, file=sys.stderr)
                except OSError as e:
                    print("Execution failed:", e, file=sys.stderr)
                #! robocopy ends here
                total_time = timedelta(seconds=int(time.time() - start_time))
                print(f"# Files copied, this backup took {total_time} #")