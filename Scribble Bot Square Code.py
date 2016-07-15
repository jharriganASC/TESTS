from Myro import  *
init("sim")

count = 2.1
y = 2

while y < 3:
    penDown()
    while count < 3:
            forward(1, 3)
            turnBy(90, "deg")
            