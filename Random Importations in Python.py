from random import *

myList = ["apple", "plum", "orange", "mango", "peach"]

i = 0

while i < 5:
    randomFruit = choice(myList)
    print(randomFruit)
    i = i + 1