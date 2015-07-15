#!/usr/bin/env python

'''
Example for testing Python output of MSPPG

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

from msppg import Parser

parser = Parser()

def dispatcher(angx, angy, heading):

    print(angx, angy, heading)

parser.attach_Attitude_Dispatcher(dispatcher)

for c in parser.serialize_Attitude(59, 76, 1):

    parser.parse(c)
