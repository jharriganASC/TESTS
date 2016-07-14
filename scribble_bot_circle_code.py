from Myro import *
init("sim")

count = 2.1
y = 2

while y < 3:
    penDown()
    while count < 3:
        motors(-70, 1, 2)
        motors(90, 0, -2)
        motors(15, 7)