from Myro import *
init("sim")

count = 2.1
y = 2

while y < 3:
    penDown()
    while count < 3:
        motors(-7, 1, 2)
        motors(9, 0, -2)
        motors(1.5, 7)