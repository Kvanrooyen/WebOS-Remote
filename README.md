# WebOS-Remote

A python application to control your LG WebOS TV with the PyWebOSTV api

## Getting started

In order to run the python file you will need to do a few things.

1.  `pip install pywebostv` and `pip install wakeonlan`
2.  Add your TV's IP address and MAC Address to the file, so it can connect.

Once you have completed the above 2 steps you can run the program. After your first run you may want to print out the registration key. I have it commented currently, just uncomment it and then you can copy paste the result into `store`. This will allow you to connect once, and not be prompted every single time you try yo connect. After you are connected you can comment out the `print(store)`

## Credit

This project would not be possible without the use of [supersaiyanmode project](https://github.com/supersaiyanmode/PyWebOSTV). I used his code from the README to connect, and then used some of the control api's.
