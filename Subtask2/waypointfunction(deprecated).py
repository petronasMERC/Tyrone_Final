#!/usr/bin/env pybricks-micropython

#Проприетарное программное обеспечение Коннора
#♥♥♥ Сделано с любовью ♥♥♥
#Тайрон версия 1.3

import math
#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
#функция чтобы перемещать Тайрона по точкам  Х и У 
#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥

def waypoint(coordlist,tyrone,ultrass):
    
    """Function takes a two dimensional list, called coordlist, of points to travel too, and a drivebase object, called tyrone to move
    the robot through multiple waypoints.
    """
    xnaught = 0
    ynaught = 0
    quadrant = -1
    for i in range(len(coordlist)):
        if (coordlist[i][0]-xnaught)> 0:
            if (coordlist[i][1]-ynaught)>0:
                quadrant = 1
            else:
                quadrant = 4
        elif (coordlist[i][0]-xnaught)<0:
            if (coordlist[i][1]-ynaught)>0:
                quadrant = 2
            else:
                quadrant = 3
        else:
            quadrant = None


        if (coordlist[i][0]-xnaught)!= 0:
            turnangle = math.degrees(math.atan(coordlist[i][1]-ynaught)/(coordlist[i][0]-xnaught))
        elif (coordlist[i][1]-ynaught) > 0:
            turnangle = 0
        else:
            turnangle = 180

        if (coordlist[i][1]-ynaught)!= 0 and (coordlist[i][0]-xnaught)!=0:
            if quadrant == 2:
                turnangle = 270+abs(turnangle)
            elif quadrant == 3:
                turnangle = 180+abs(turnangle)
            elif quadrant == 4:
                turnangle = 90+abs(turnangle)
        else:
            if (coordlist[i][0]-xnaught) < 0 and (coordlist[i][1]-ynaught) == 0:
                turnangle = -90
            elif (coordlist[i][0]-xnaught) > 0 and (coordlist[i][1]-ynaught) == 0:
                turnangle = 90
        tyrone.turn(turnangle)
        distance = math.sqrt(((coordlist[i][0]-xnaught)**2)+((coordlist[i][1]-ynaught)**2))
        tyrone.straight(distance)
        if ultrass.distance()<250:
            object_avoidance(tyrone)
        print(distance)
        tyrone.turn(0-turnangle)
        xnaught = coordlist[i][0]
        ynaught = coordlist[i][1]
        

