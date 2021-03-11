# Exersize

# bool(0)
# bool("")
# bool("hello")
# bool(1)
# bool(None)
# bool([])
# bool([1,2,3])

# __________________________________________

# Exercise: Conditionals Syntax

# Practice #1
temp = 40

if temp < 50:
    print("It's a bit chilly outside")
    
# __________________________________________

# Practice #2
temp = 100

if temp < 50:
    print("It's a bit chilly outside")
else:
    print("It's pleasant outside")
# __________________________________________

# Practice #3
temp = 0

if temp == 0:
    print("It's ZERO DEGREES outside!") 
elif temp == 100:
    print("It's ONE HUNDDRED DEGREES outside!")
elif temp < 50:
    print("It's a bit chilly outside") 
elif temp < 100:
    print("It's warm outside")    
# __________________________________________

# Black Jack game
score = 21

if score < 17:
    print("Hit Me!")
elif score < 21:
    print("Great Hand!")
elif score > 21:
    print("Bust!")
else:
    print("Black Jack!")

# __________________________________________

# Exercise: Divisible by 5
x = 11

if x%5 == 0:
    print(f"{x} is divisible by 5")
else:
    print(f"{x} is not divisible by 5")

# __________________________________________

# Exercise
# coffee = True
# good_sleep = True

# coffee = False
# good_sleep = True

# coffee = True
# good_sleep = False

coffee = False
good_sleep = False

if coffee and good_sleep:
    print("It's going to be a great day!")
else:
    print("Eh. Today's going to be a wash.")

# __________________________________________

# Practice Problems
#Diagram to code
x = 7
y = 5
if x==y:
  print ('equal')
elif x<y:
  print ('less')
else:
  print ('grater')

# __________________________________________

# Code to diagram
if number_of_sides == 1:
    print("You've got a line")
elif number_of_sides == 2:
    print("I'm not really sure what you have")
elif number_of_sides == 3:
    print "You've got a triangle"
elif number_of_sides == 4:
    print("You've got some sort of quadrilateral")

# __________________________________________

# Diagram and Output Prediction

# problem 1
cookies = True
cake = False

if cookies:
    print("OMG COOKIEZ")

if cake:
    print("OMG CAKE!")
else:
    print("WHATEVZ DESSERTZ.")

# __________________________________________

# problem 2
person_age = 55
ada_age = 6

if person_age < ada_age:
    print("This person is younger")
elif ada_age < person_age:
    print("Ada is younger")
else:
    print("They’re the same!")

# __________________________________________

# problem 3
pet = "cat"
food = "ice cream"

if pet == "cat":
    print("here kitty")
elif pet == "dog":
    print("woof")
else:
    print("some other sound")

if food == "broccoli":
    print("eh.")
elif food == "ice cream":
    print("yum")

# __________________________________________

# problem 4
x = 7
y = 7

if x >= y:
    if x > y:
        print("x is bigger")
    else:
        print("x = y")
else:
    print("y is bigger")

# __________________________________________

# problem 5
x = 7
y = 7

if x > y or x == y:
    if x > y:
        print("x is bigger")
    else:
        print("x = y")
else:
    print("y is bigger")

# __________________________________________

# problem 6
x = 7
y = 7

if x >= y:
    print("x is bigger")
else:
    print("y is bigger")

if x == y:
    print("x = y")
