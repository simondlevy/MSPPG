#!/usr/bin/env python

'''
getimu.py Uses MSPPG to request and handle ATTITUDE messages from flight controller IMU

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

BAUD = 57600

from msppg import MAVLink_Parser as Parser
import serial
from math import degrees

from sys import argv

if len(argv) < 2:

    print('Usage: python %s PORT' % argv[0])
    print('Example: python %s /dev/ttyACM0' % argv[0])
    exit(1)

parser = Parser()
port = serial.Serial(argv[1], BAUD)

def rad2deg(rad):

    return '%+3.3f' % degrees(rad)

def handler(time_boot_ms, roll, pitch, yaw, rollspeed, pitchspeed, yawspeed):

    print('Roll=%s  Pitch=%s  Yaw=%s' % (rad2deg(roll), rad2deg(pitch), rad2deg(yaw)))

parser.set_ATTITUDE_Handler(handler)

while True:

    try:

        parser.parse(port.read(1))

    except KeyboardInterrupt:

        break

