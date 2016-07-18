from Myro import *
init("sim")

def firstInitial():
    penDown()
    forward(1,1)
    turnBy(90, "deg")
    forward(1, 2)

firstInitial()



penUp()


def secondInitial():
    turnBy(90, "deg")
    backward(1, 1)
    penDown()
    turnBy(90, "deg")
    forward(1, 2)
    turnBy(180, "deg")
    forward(1, 1)
    turnBy(90, "deg")
    backward(1, .5)
    turnBy(90, "deg")
    forward(1, 1)
    turnBy(180, "deg")
    forward(1, 2)
    
secondInitial()    