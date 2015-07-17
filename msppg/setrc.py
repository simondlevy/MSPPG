#!/usr/bin/env python

'''
setrc.py Uses MSPPG to set raw RC values in flight controller

Copyright (C) Rob Jones, Alec Singer, Chris Lavin, Blake Liebling, Simon D. Levy 2015

This code is free software: you can redistribute it and/or modify
it under the terms of the GNU Lesser General Public License as 
published by the Free Software Foundation, either version 3 of the 
License, or (at your option) any later version.
This code is distributed in the hope that it will be useful,     
but WITHOUT ANY WARRANTY without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU Lesser General Public License 
along with this code.  If not, see <http:#www.gnu.org/licenses/>.
'''

BAUD = 115200
UPDATE_RATE_HZ = 200

from msppg import Parser
import serial
import time
from sys import argv
import threading

if len(argv) < 2:

    print('Usage: python %s PORT' % argv[0])
    print('Example: python %s /dev/ttyUSB0' % argv[0])
    exit(1)

parser = Parser()
port = serial.Serial(argv[1], BAUD)

setmsg = parser.serialize_SET_RAW_RC(1500, 1500, 1500, 1200, 0, 0, 0, 0)
getmsg = parser.serialize_RC_Request()

switchprev = -1

def setter(state):

    while(True):

        print(state)

        if state[0]:

            port.write(setmsg)

        time.sleep(1./UPDATE_RATE_HZ)


state = [0,0,0] # flag, current switch, previous switch

thread = threading.Thread(target=setter, args=(state,))
thread.setDaemon(True)
thread.start()

def getter(c1, c2, c3, c4, c5, c6, c7, c8):

    #print(c1, c2, c3, c4, c5)

    if c5 > 1000:

        state[0] = 1

    sate[1] = c5

    port.write(getmsg)

parser.set_RC_Handler(getter)

port.write(getmsg)

while True:

    try:

        parser.parse(port.read(1))

    except KeyboardInterrupt:

        break
