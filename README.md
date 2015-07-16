# MSPPG
Multiwii Serial Protocol Parser Generator for Python, Java, and C++

The script msppg.py is ready to-run using your favorite Python interpreter: command-line, IDLE, etc.  To install so you can run it anywhere, do

% python setup.py install

from a Windows command shell, or

% sudo python setup.py install

in Unix (Linux, OS X).

Once the package is installed, you can put your example.json file anywhere and run the following:

% msppg.py example.json

which will create output/python, output/java/ and output/cpp. You can cd to any of those directories and do

% make test

to test the code.  In output/python you can also run the imutest.py program, which uses Tkinter and NumPy to visualize the Attitude messages coming from a flight controller (tested with AcroNaze running Baseflight).  In output/java you can do

% make jar

to build the msppg.jar file, which can then be used as a library for Android projects and other Java-based work.

The Arduino example allows you to control the pitch of a buzzer using the pitch from the IMU.  To run that example, drag the output/arduino/MSPPG folder into your Arduino libaries folder, launch the Arduino IDE, and find the MSPPG submenu under the File/Examples menu.

The example.json file currently contains only one message specification (Attitude), but you can easily add to it by specifying additional messages from the MSP: http://www.multiwii.com/wiki/index.php?title=Multiwii_Serial_Protocol. 
MSPPG currently supports types byte, short, and float, but we will likely add int as the need arises.
