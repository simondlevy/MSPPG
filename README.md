# MSPPG
Multiwii Serial Protocol Parser Generator

Install as usual:

% python setup.py install

or

% sudo python setup.py install

Once the package is installed, you can put your example.json file anywhere and run the following:

% msppg.py example.json

which will create output/python, output/java/ and output/cpp. You can cd to any of those directories and do

% make test

to test the code.  In output/python you can also run the imutest.py program, which uses Tkinter and NumPy to visualize the Attitude messages coming from an a flight controller (tested with AcroNaze running Baseflight).  In output/java you can do

% make jar

to build the msppg.jar file, which can then be used as a library for Android projects and other Java-based work.
