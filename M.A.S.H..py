from random import *

Spouse = ["John Bellion", "Kate Upton", "Chris Hemsworth", "Beyonce"]

Jobs = ["Rapper", "Doctor", "Teacher", "Executive", "Jailer"]

Cars = ["Ferrari F12 TDF", "Nissan Altima", "Lamborghini Huracan", "Koenigsegg One:1", "Nissan Juke"]

Home = ["mansion", "apartment", "shack", "house"]



mySpouse = raw_input("Who do you want to be your spouse?")

randomSpouse = choice(Spouse)


myJobs = raw_input("What kind of job would you like?")

randomJob = choice(Jobs)
   
  

myCars = raw_input("What kind of car would you like?")

randomCar = choice(Cars)
   
    
   


randomHome = choice(Home)









print("Your spouse is" , randomSpouse)
print("Your job is" , randomJob)
print("You'll have a" , randomCar)
print("You'll live in a" , randomHome)