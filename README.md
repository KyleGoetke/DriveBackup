# RemovableDriveBackup

This script detects any connected removable drives and, given confirmation by the user, copies all contents of a drive to a predetmined folder.

## Updates

#### v0.2 - April 20, 2022

Changed copying service from [`distutils.dir_util.copy_tree`](https://docs.python.org/3/distutils/apiref.html#module-distutils.dir_util) to [`robocopy`](https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/robocopy)

Changed `dest_path` to match production environment

Added simple error handling for robocopy, still WIP

#### v0.1 - April 19, 2022

Script created!

Configured to copy from a flash drive to development environment
