#!/usr/bin/env pybricks-micropython
from pybricks.hubs import EV3Brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import Port, Stop, Direction, Button, Color
from pybricks.tools import wait, StopWatch, DataLog
from pybricks.robotics import DriveBase
from pybricks.media.ev3dev import SoundFile, ImageFile

import time
# Initialize the EV3 brick.
ev3 = EV3Brick()
# Initialize a motor at port B.
motor1 = Motor(Port.B, Direction.COUNTERCLOCKWISE)
motor2 = Motor(Port.C)
rotation_motor = Motor(Port.A)
sensor = ColorSensor(Port.S4)



bar = 2000
half = bar/2
fourth = bar/4
eighth = bar/8
sixteenth = bar/16
thirtysecond = bar/32


def play (frequency, duration, fill = 0):
    ev3.speaker.beep(frequency, duration/(4/2))
    ev3.speaker.beep(0, duration/(4/2))

def pause (duration):
    ev3.speaker.beep(0, duration)

A = [27.5]
B = []
H = []
C = []
Db = []
D = []
Eb = []
E = []
F = []
Gb = []
G = []
Ab = []


nulpunkt = rotation_motor.angle()
maks = 40

rotation_motor.run_target(100, nulpunkt)






for i in range(1, 100):
    current = round(A[0] * 2 ** (i/12), 2)
    if (i % 12 == 0):
        A.append(current)
    elif (i % 12 == 1):
        B.append(current)
    elif (i % 12 == 2):
        H.append(current)
    elif (i % 12 == 3):
        C.append(current)
    elif (i % 12 == 4):
        Db.append(current)
    elif (i % 12 == 5):
        D.append(current)
    elif (i % 12 == 6):
        Eb.append(current)
    elif (i % 12 == 7):
        E.append(current)
    elif (i % 12 == 8):
        F.append(current)
    elif (i % 12 == 9):
        Gb.append(current)
    elif (i % 12 == 10):
        G.append(current)
    elif (i % 12 == 11):
        Ab.append(current)

timer = StopWatch()

yellow = 0
red = 0
black = 0

def color_config(color):
    while True:
        pressed = ev3.buttons.pressed()
        ev3.screen.clear()
        if(color == "Yellow"):
            ev3.screen.draw_text(40, 50, "Configure: Yellow")
        elif (color == "Red"):
            ev3.screen.draw_text(40, 50, "Configure: Red")
        else:
            ev3.screen.draw_text(40, 50, "Configure: Black")
        wait(5)
        if pressed:
            ev3.screen.clear()
            return sensor.rgb()
            break



black = color_config("Black")
wait(1000)
red = color_config("Red")
wait(1000)
yellow = color_config("Yellow")
wait(1000)
while True:
    if ev3.buttons.pressed():
        break


z = 5

def find_boundaries(color):
    boundaries = []
    individual_points = []
    for j in range(0,2 + 1):
        for i in range(color[j] - z, color[j] + z + 1):
            individual_points.append(i)
        boundaries.append(individual_points)
        individual_points = []
    return boundaries

yellow_boundaries = find_boundaries(yellow)
black_boundaries = find_boundaries(black)
red_boundaries = find_boundaries(red)



while True:
    yellow_count = 0
    d0 = time.time() 
    if(red_boundaries[0].count(sensor.rgb()[0]) == 1 and red_boundaries[1].count(sensor.rgb()[1]) == 1 and red_boundaries[2].count(sensor.rgb()[2]) == 1):
        
        rotation_motor.run_target(1000, nulpunkt - maks)
        wait(50)
    elif(black_boundaries[0].count(sensor.rgb()[0]) == 1 and black_boundaries[1].count(sensor.rgb()[1]) == 1 and black_boundaries[2].count(sensor.rgb()[2]) == 1):
        
        rotation_motor.run_target(1000, nulpunkt + maks)
        wait(50)
    elif(yellow_boundaries[0].count(sensor.rgb()[0]) == 1 and yellow_boundaries[1].count(sensor.rgb()[1]) == 1 and yellow_boundaries[2].count(sensor.rgb()[2]) == 1):
        yellow_count += 1
        wait(1)
        if(yellow_count > 10):
            d1 = time.time()
            motor1.stop()
            motor2.stop()
            ev3.screen.draw_text(40, 50, (d1-d0))
        else:
            yellow_count = 0
    else:
        motor1.run(500)
        motor2.run(500)
        rotation_motor.run_target(1000, nulpunkt)


    # play(D[4], sixteenth)
    # play(D[4], sixteenth)
    # play(D[5], eighth)
    # play(A[5], eighth)
    # pause(sixteenth)
    # play(Ab[4], eighth)
    # play(G[4], eighth)
    # play(F[4], eighth)
    # play(D[4], sixteenth)
    # play(F[4], sixteenth)
    # play(G[4], sixteenth)

    # play(C[4], sixteenth)
    # play(C[4], sixteenth)
    # play(D[5], eighth)
    # play(A[5], eighth)
    # pause(sixteenth)
    # play(Ab[4], eighth)
    # play(G[4], eighth)
    # play(F[4], eighth)
    # play(D[4], sixteenth)
    # play(F[4], sixteenth)
    # play(G[4], sixteenth)

    # play(H[4], sixteenth)
    # play(H[4], sixteenth)
    # play(D[5], eighth)
    # play(A[5], eighth)
    # pause(sixteenth)
    # play(Ab[4], eighth)
    # play(G[4], eighth)
    # play(F[4], eighth)
    # play(D[4], sixteenth)
    # play(F[4], sixteenth)
    # play(G[4], sixteenth)

    # play(B[4], sixteenth)
    # play(B[4], sixteenth)
    # play(D[5], eighth)
    # play(A[5], eighth)
    # pause(sixteenth)
    # play(Ab[4], eighth)
    # play(G[4], eighth)
    # play(F[4], eighth)
    # play(D[4], sixteenth)
    # play(F[4], sixteenth)
    # # play(G[4], sixteenth)








