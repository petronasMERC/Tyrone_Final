#!/usr/bin/env pybricks-micropython

#Проприетарное программное обеспечение Коннора
#♥♥♥ Сделано с любовью ♥♥♥
#Тайрон версия 1.3

import math
import time

#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
#функция чтобы перемещать Тайрона по точкам  Х и У
#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥

def smartturn(tyrone,gyro,rightMotor,leftMotor,degrees,ultrass):
    """Precision turning due to the error created by simply using the functions
    provided to us in the pybricks library. This is specific to the Robot and uses the gyroscopic sensor.
    """
    gyro.reset_angle(0)
    if degrees > 0:
        while gyro.angle()<degrees:
            tyrone.drive(0,20)
        tyrone.stop()
        rightMotor.brake()
        leftMotor.brake()
    elif degrees < 0:
        while gyro.angle()>degrees:
            tyrone.drive(0,-20)
        tyrone.stop()
        rightMotor.brake()
        leftMotor.brake()

    else:
        return


def smartdrive(tyrone, gyro, rightMotor,leftMotor,dist,ultrass,recursion=False):
    """Precision forward movement, correcting any drift off 0 degrees using the gyroscopic sensor"""
    if recursion == False:
        tyrone.reset()
        errordist = 0
        correction = 0
        gyro.reset_angle(0)
    while tyrone.distance() <= dist:
        if ultrass.distance()< 300:
            tyrone.stop()
            rightMotor.brake()
            leftMotor.brake()
            errordist = dist-tyrone.distance()
            while ultrass.distance()<300:
                time.sleep(.2)
            smartdrive(tyrone,gyro,rightMotor,leftMotor,errordist,ultrass,recursion=True)
        correction = (0-gyro.angle())*2
        print(gyro.angle())
        tyrone.drive(100,correction)
    tyrone.stop()
    rightMotor.brake()
    leftMotor.brake()
 

def waypoint(coordlist,tyrone,ultrass,rightMotor,leftMotor,gyro,correctlast=True):
    
    """Function takes a two dimensional list, called coordlist, of points to travel too, and a drivebase object, called tyrone to move
    the robot through multiple waypoints.
    """
    xcurrent = 0
    ycurrent = 0
    adjustedx = 0
    adjustedy = 0
    turncorrect = 0

    for i in range(len(coordlist)):
        adjustedx = coordlist[i][0] - xcurrent
        print(adjustedx)
        adjustedy = coordlist[i][1] - ycurrent
        print(adjustedy)
        if adjustedx != 0:
            if adjustedx > 0:
                smartturn(tyrone,gyro,rightMotor,leftMotor,90,ultrass)               
                turncorrect = -90
                time.sleep(.5)
            else:
                smartturn(tyrone,gyro,rightMotor,leftMotor,-90,ultrass)
                turncorrect = 90
                time.sleep(.5)

        if adjustedy < 0:
            smartturn(tyrone,gyro,rightMotor,leftMotor,180,ultrass)
            turncorrect = 180
            time.sleep(.5)

        adjustedy = abs(adjustedy)
        adjustedx = abs(adjustedx)

        if adjustedx == 0:
            smartdrive(tyrone,gyro,rightMotor,leftMotor,adjustedy,ultrass)
            time.sleep(.5)


        if adjustedy == 0:
            smartdrive(tyrone,gyro,rightMotor,leftMotor,adjustedx,ultrass)
            time.sleep(.5)
 
        if correctlast==False and i==len(coordlist)-1:
            return
        else:
            if turncorrect != 0:
                smartturn(tyrone,gyro,rightMotor,leftMotor,turncorrect,ultrass)
                time.sleep(.5)
                print("turned", turncorrect, "degrees to correct")

        turncorrect = 0
        xcurrent = coordlist[i][0]
        ycurrent = coordlist[i][1]
