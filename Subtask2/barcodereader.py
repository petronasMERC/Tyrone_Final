#!/usr/bin/env pybricks-micropython

#Проприетарное программное обеспечение Коннора
#♥♥♥ Сделано с любовью ♥♥♥
#Тайрон версия 1.4

from pybricks.parameters import Port, Stop, Direction, Button, Color
import time
import math
#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥
#функция чтобы читать щтрих-код
#♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥♥

def read(tyrone,colorRight,barcodedb):
    """Function to move along side of a package for the purpose of reading it's barcode. It is intended to check barcodes
    against the barcode database
    """
    barcode = []
    prebarcode = []
    barcodedebug = []
    iterations = 0
    sizes = 0
    for i in range(4000):
        tyrone.drive(30,0)
        if colorRight.color()==Color.BLACK:
            prebarcode.append('1')
        if colorRight.color()==Color.WHITE:
            prebarcode.append('0')
        barcodedebug.append(colorRight.color())
        iterations += 1

    
    tyrone.stop()
    #barcode[0] = prebarcode[0]
    onetofour = 1
    sizes = math.floor(len(prebarcode)/4)
    v1 = prebarcode[1:sizes]
    v2 = prebarcode[sizes:sizes*2]
    v3 = prebarcode[sizes*2:sizes*3]
    v4 = prebarcode[sizes*3:sizes*4]
    
    onecount = 0
    zerocount = 0

    for i in range(len(v1)):
        if v1[i]=='1':
            onecount +=1
        else:
            zerocount +=1
    if onecount > zerocount:
        barcode.append('1')
    else:
        barcode.append('0')

    onecount = 0
    zerocount = 0

    for i in range(len(v2)):
        if v2[i]=='1':
            onecount +=1
        else:
            zerocount +=1
    if onecount > zerocount:
        barcode.append('1')
    else:
        barcode.append('0')
    
    onecount = 0
    zerocount = 0
    
    for i in range(len(v3)):
        if v3[i]=='1':
            onecount +=1
        else:
            zerocount +=1
    if onecount > zerocount:
        barcode.append('1')
    else:
        barcode.append('0')

    onecount = 0
    zerocount = 0

    for i in range(len(v4)):
        if v4[i]=='1':
            onecount +=1
        else:
            zerocount +=1
    if onecount > zerocount:
        barcode.append('1')
    else:
        barcode.append('0')

    barcode.reverse
    barcode = int(''.join(barcode))
    print(v1)
    print('----------')
    print(v2)
    print('----------')
    print(v3)
    print('----------')
    print(v4)
    print(barcode)
    tyrone.straight(-160)
    return barcode