# MSPPG
Multiwii Serial Protocol Parser Generator

The script msppg.py is ready to-run using your favorite Python interprter: command-line, IDLE, etc.  To install so you can run it anywhere, do

% python setup.py install

from a Windows command shell, or

% sudo python setup.py install

in Unix (Linux, OS X).

Once the package is installed, you can put your example.json file anywhere and run the following:

% msppg.py example.json

which will create output/python, output/java/ and output/cpp. You can cd to any of those directories and do

% make test

to test the code.  In output/python you can also run the imutest.py program, which uses Tkinter and NumPy to visualize the Attitude messages coming from an a flight controller (tested with AcroNaze running Baseflight).  In output/java you can do

% make jar

to build the msppg.jar file, which can then be used as a library for Android projects and other Java-based work.

The example.json file currently contains only one message specification (Attitude), but you can easily add to it by specifying additional messages from the MSP: http://www.multiwii.com/wiki/index.php?title=Multiwii_Serial_Protocol.
