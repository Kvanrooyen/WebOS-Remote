# WebOS-Remote

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT) ![GitHub last commit](https://img.shields.io/github/last-commit/Kvanrooyen/WebOS-Remote.svg) ![Maintenance](https://img.shields.io/maintenance/yes/2019.svg)

A python application to control your LG WebOS TV with the PyWebOSTV api

## Getting started

In order to run the python file you will need to do a few things.

1.  `pip install pywebostv` and `pip install wakeonlan`
2.  Add your TV's IP address and MAC Address to the file, so it can connect.

Once you have completed the above 2 steps you can run the program. After your first run you may want to print out the registration key. I have it commented currently, just uncomment it and then you can copy paste the result into `store`. This will allow you to connect once, and not be prompted every single time you try yo connect. After you are connected you can comment out the `print(store)`

## Credit

This project would not be possible without the use of [supersaiyanmode project](https://github.com/supersaiyanmode/PyWebOSTV). I used his code from the README to connect, and then used some of the control api's.

## Creating a executeable file
If you would like to run this program on another machine that does not have python, you can create an executeable file. I have made a cmd script that you can run, to install the necessary modules, and then create it. The file will be caleed remote.exe and it will be in a folder dist. To create the executeable file, double click the file called 'Create exe.bat' (This file will only work on Windows machines.)

After the file has finished runnin, you directry will look like this:
```
───WebOS-Remote
   │   Create exe.bat
   │   remote.py
   │   remote.spec
   │
   ├───build
   │   └───run
   │           Analysis-00.toc
   │           base_library.zip
   │           EXE-00.toc
   │           PKG-00.pkg
   │           PKG-00.toc
   │           PYZ-00.pyz
   │           PYZ-00.toc
   │           run.exe.manifest
   │           Tree-00.toc
   │           Tree-01.toc
   │           warn-run.txt
   │           xref-run.html
   │
   ├───dist
   │       remote.exe
   │
   └───__pycache__
           remote.cpython-37.pyc
```
The newly created executeable will be in the dist folder. You can now use that without needing python to be installed.
