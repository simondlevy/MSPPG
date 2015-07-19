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

BAUD            = 115200
UPDATE_RATE_HZ  = 200
WAIT_TIME_SEC   = .1

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

class SetterThread(threading.Thread):

    def __init__(self, getter):

        threading.Thread.__init__(self, target=self.setter)

        self.setDaemon(True)

        self.getter = getter

    def setter(self):

        while(True):

            if self.getter.autopilot: 

                throttle = int(1200 + self.getter.throttle * 500)
                message = parser.serialize_SET_RAW_RC(1500, 1500, 1500, throttle, 1500, 0, 0, 0)
                port.write(message)

            time.sleep(1./UPDATE_RATE_HZ)

class Getter:

    def __init__(self):

        self.c5prev = 0

        self.request = parser.serialize_RC_Request()

        port.write(self.request)

        parser.set_RC_Handler(self.get)

        self.armed = False
        self.autopilot = False
        self.offtime = 0
        self.timestart = time.time()

    def _error(self, msg):

        print(msg)
        exit(1)

    def get(self, c1, c2, c3, c4, c5, c6, c7, c8):

        # Disallow startup with switch down
        if self.offtime == 0 and c5 > 1000:
            self._error('Please turn off switch before starting')

        # Check arming

        if c3 > 2000 and c4 < 990:
            self.armed = True

        if c3 < 990 and c4 < 990:
            self.armed = False

        # Switch moved down
        if c5 > 1000 and self.c5prev < 1000 and self.offtime > WAIT_TIME_SEC and self.armed:

            self.autopilot = True
            self.throttle = 0
            self.throttledir = +1

        # Switch moved back up
        if c5 < 1000 and self.c5prev > 1000:

            self.autopilot = False

            self.timestart = time.time()

        if self.autopilot:

            # Increase / decrease throttle
            self.throttle += self.throttledir * .001

            # Change throttle direction when limit reached
            if self.throttle <= 0:
                self.throttledir = +1
            elif self.throttle >= 0.5:
                self.throttledir = -1

        else: 

            self.offtime = time.time() - self.timestart

        self.c5prev = c5

        port.write(self.request)

getter = Getter()

setter = SetterThread(getter)

setter.start()

while True:

    try:

        parser.parse(port.read(1))

    except KeyboardInterrupt:

        break
