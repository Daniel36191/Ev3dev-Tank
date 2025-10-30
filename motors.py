#!/usr/bin/env python3

from ev3dev2.motor import list_motors

# List all connected motors
motors = list_motors()
print("Found {} motor(s):".format(len(motors)))
for i, motor in enumerate(motors):
    print("Motor {}:".format(i))
    print("  Address: {}".format(motor.address))
    print("  Driver: {}".format(motor.driver_name))
    print("  Commands: {}".format(motor.commands))