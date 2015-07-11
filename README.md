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

to test the code.
