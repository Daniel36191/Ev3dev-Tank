#!/usr/bin/env python3

# Import the necessary libraries
import time
import math
from ev3dev2.motor import *
from ev3dev2.sound import Sound
from ev3dev2.button import Button
from ev3dev2.sensor import *
from ev3dev2.sensor.lego import *
from ev3dev2.sensor.virtual import *

# Create the sensors and motors objects
motorA = LargeMotor(OUTPUT_A)
motorB = LargeMotor(OUTPUT_B)
left_motor = motorA
right_motor = motorB
tank_drive = MoveTank(OUTPUT_A, OUTPUT_B)
steering_drive = MoveSteering(OUTPUT_A, OUTPUT_B)

spkr = Sound()
btn = Button()
radio = Radio()
obtr = ObjectTracker()

gyro_sensor_in1 = GyroSensor(INPUT_1)

## Main Entry

step_time_fb = 3.0 ## In Seconds
step_time_lr = 1.5 ## In Seconds

## Movement Functions
def forward():
    tank_drive.on_for_seconds(left_speed=50, right_speed=50, seconds=step_time_fb, block=True)
def backward():
    tank_drive.on_for_seconds(left_speed=-50, right_speed=-50, seconds=step_time_fb, block=True)
def turn_left():
    steering_drive.on_for_seconds(steering=-100, speed=30, seconds=step_time_lr, block=True)
def turn_right():
    steering_drive.on_for_seconds(steering=100, speed=30, seconds=step_time_lr, block=True)

## Record movement sequence
def record_moves():
    global movesteps
    movesteps = []
    while True:
        if btn.up:
            movesteps.append("F")
            forward()
            time.sleep(0.5)
        elif btn.down:
            movesteps.append("B")
            backward()
            time.sleep(0.5)
        elif btn.left:
            movesteps.append("L")
            turn_left()
            time.sleep(0.5)
        elif btn.right:
            movesteps.append("R")
            turn_right()
            time.sleep(0.5)
        elif btn.enter:
            break

## Main movement sequence
def move_steps():
    i = 0
    for x in movesteps:
        i = i + 1
        if x == "F":
            forward()
        elif x == "B":
            backward()
        elif x == "L":
            turn_left()
        elif x == "R":
            turn_right()
        elif i == len(movesteps):
            print("Complete")
            break
        time.sleep(0.5)

while True:
    print("Record Moves")
    record_moves()
    print("Moves Recorded:", movesteps)
    print("Replay Moves")
    move_steps()