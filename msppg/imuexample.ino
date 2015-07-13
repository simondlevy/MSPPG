/*
Example for testing Arduino output of MSPPG

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

#include "MSPPG.h"

class My_Attitude_Handler : public Attitude_Handler {

    public:

        void handle_Attitude(short pitch, short roll, short yaw) {

            Serial.print(pitch);
            Serial.print(" " );
            Serial.print(roll);
            Serial.print(" " );
            Serial.println(yaw);
        }

};

void setup() {

    Serial.begin(9600); 

    MSP_Parser parser;

    MSP_Message message = parser.serialize_Attitude(59, 76, 1);

    My_Attitude_Handler handler;

    parser.set_Attitude_Handler(&handler);

    for (byte b=message.start(); message.hasNext(); b=message.getNext()) {

        parser.parse(b);
    }
}

void loop() {

}
