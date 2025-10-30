#!/usr/bin/env python3

#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
from ev3dev2.motor import *
# from ev3dev2.sound import Sound
from ev3dev2.button import Button
# from ev3dev2.sensor import *
# from ev3dev2.sensor.lego import *

# Create the sensors and motors objects
motorA = LargeMotor(OUTPUT_B)
motorB = LargeMotor(OUTPUT_D)
left_motor = motorA
right_motor = motorB
tank_drive = MoveTank(OUTPUT_B, OUTPUT_D)
steering_drive = MoveSteering(OUTPUT_B, OUTPUT_D)

while True:
    tank_drive.on_for_seconds(left_speed=50, right_speed=50, seconds=3, block=True)