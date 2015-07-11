/*
Example for testing C++ output of MSPPG

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
*/

#include <stdio.h>

#include <vector>
#include <iostream>
using namespace std;

#include "msppg/msppg.h"

class My_RAW_IMU_Handler : public RAW_IMU_Handler {

    public:

        void handle_Raw_IMU(short pitch, short roll, short yaw) {

            printf("%+3d %+3d %+3d\n", pitch, roll, yaw);
        }

};

int main(int argc, char ** argv) {

    MSP_Parser parser;

    MSP_Message message = parser.serialize_Raw_IMU(59, 76, 1);

    My_Raw_IMU_Handler handler;

    parser.set_Raw_IMU_Handler(&handler);

    for (byte b=message.start(); message.hasNext(); b=message.getNext()) {

        parser.parse(b);
    }

    return 0;
}
