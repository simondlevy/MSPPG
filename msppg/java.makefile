#
# Example Makefile for DolphinLink Java output
#
# Copyright (C) Simon D. Levy 2015
#
# This code is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as 
# published by the Free Software Foundation, either version 3 of the 
# License, or (at your option) any later version.
#
# This code is distributed in the hope that it will be useful,     
# but WITHOUT ANY WARRANTY without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
#  You should have received a copy of the GNU Lesser General Public License 
#  along with this code.  If not, see <http:#www.gnu.org/licenses/>.
#  You should also have received a copy of the Parrot Parrot AR.Drone 
#  Development License and Parrot AR.Drone copyright notice and disclaimer 
#  and If not, see 
#   <https:#projects.ardrone.org/attachments/277/ParrotLicense.txt> 
# and
#   <https:#projects.ardrone.org/attachments/278/

# Change this to match your desired install directory
INSTALLDIR = /home/levys/DolphinQuad/gcs/android/DolphinGCS/app/src/main/java/edu/wlu/dolphingcs/

ALL = example.class

all: $(ALL)

install:
	cp -r edu/wlu/dolphingcs/dolphinlink $(INSTALLDIR)

test: example.class
	java example
  
example.class: example.java
	javac example.java
