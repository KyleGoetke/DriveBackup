# DriveBackup

This script searches connected drives and, once the target is found (`E:\` by default), all contents of the drive are copied to a predetermined folder.

## Updates

#### v0.3 - April 22, 2022

Adjusted drive checking, only proceeds if `E:\` is detected

Added verbose output + time delays

#### v0.2 - April 20, 2022

Changed copying service from [`distutils.dir_util.copy_tree`](https://docs.python.org/3/distutils/apiref.html#module-distutils.dir_util) to [`robocopy`](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)

Changed `dest_path` to match production environment

Added simple error handling for robocopy, still WIP

#### v0.1 - April 19, 2022

Script created!

Configured to copy from a flash drive to development environment
