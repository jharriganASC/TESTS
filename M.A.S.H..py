from random import *

Wives = ["Taylor Swift", "Hillary Clinton", "Scarlett Johansson", "Beyonce"]

Jobs = ["Rapper", "Doctor", "Teacher", "Executive", "Jailer"]

Cars = ["Ferrari F12 TDF", "DaeWoo", "Lamborghini Huracan", "Koenigsegg One:1", "Nissan Juke"]

Home = ["mansion", "apartment", "shack", "house"]



myWives = raw_input("Who do you want to be your wife?")

randomWife = choice(Wives)


myJobs = raw_input("What kind of job would you like?")

randomJob = choice(Jobs)
   
  

myCars = raw_input("What kind of car would you like?")

randomCar = choice(Cars)
   
    
   


randomHome = choice(Home)


print("Your wife is" , randomWife)
print("Your job is" , randomJob)
print("You'll have a" , randomCar)
print("You'll live in a" , randomHome)