# I'm a code comment. Python knows this is for people and not computers
# Also, it is always taco time.
taco_time = "Always"

# This is a comment too.
print("But this isn't.") # comments can be on the same line as code

#This comment is not following good Python style practices because it does not have space after the #

# ___________________________________________________

# Determining the type
type(1)

x = 1
type(x)

type("hello")

word = "hello"
type(word)

# What is a class?
print(type(1))

# ___________________________________________________

# Mathematical Operations
2 / 3
2 // 3
10 % 3
2 * 3 + 5

# ___________________________________________________

# Assignment Statements

# the value of 5 is assigned to the variable named x
x = 5
# the current value of x (5) is added to 1
# that sum is then assigned to the variable named x
x = x + 1
print("x =", x)

# ___________________________________________________

# the value of 1 is assigned to the variable named x
x = 1
# the value stored in x is assigned to y
# note: this does not mean that x and y will always
# store the same value
y = x
# the value of 3 is assigned to the variable named x
x = 3
# note: y still holds the value of 1
print("x =", x)
print("y =", y)

# _______________________________________________________________

# the value of "Rosa" is assigned to the variable named dog_name
dog_name = "Rosa"
# the value of "Raquel" is assigned to the variable named cat_name
cat_name = "Raquel"
# the value of 7 is assigned to the variable named dog_age
dog_age  = 7
# the value of 11 is assigned to the variable named cat_age
cat_age  = 11

print("The dog named", dog_name, "is", dog_age, "years old")
print("The cat named", cat_name, "is", cat_age, "years old")

# _______________________________________________________________

# Expressions checking
x = 2
y = 5

# x += 3 
# x += y + 3
# x -= 2
# x -= y - 5
# x /= 3
# x //= 3
# x *= y
# x %= y

print("x =", x)
print("y =", y)

# _______________________________________________________________

# Strings

# Methd capitalize
# store the name of a state in the variable state_name
state_name = "washington"

# use string interpolation and the method capitalize to output the state_name in a different string
print(f"{state_name.capitalize()} is a nice place to live!")

# _______________________________________________________________

# Methd isdigit
# store a value in the variables value_1 and value_2
value_1 = "2"
value_2 = "hello"

# use string interpolation and the method capitalize to output whether or not the values are digits.
print(f"True or False? The value {value_1} is a digit: {value_1.isdigit()}")
print(f'True or False? The value {value_2} is a digit: {value_2.isdigit()}')

#________________________________________________________________

#Exersizes

# Exersize number 1
# Assign values to three variables x1, x2, and x3.
# Print three number equations that show the result of adding 20 to each of the variables.
# For instance, if x1 = 25, the ouput of our code should be 25 + 20 = 45.

# assign values to 3 variables
x1 = 1000
x2 = 2034
x3 = 11111

# add 20
amount = 20
sum1 = x1+amount
sum2 = x2+amount
sum3 = x3+amount

# print the equations
print(f"{x1} + 20 = {sum1}" )
print(f"{x2} + 20 = {sum2}" )
print(f"{x3} + 20 = {sum3}" )

#________________________________________________________________

# Common Escape Sequences

# double quotes.
phrase = "\"We're so glad you're here!\" they said.\n"
print(phrase) 
 
# new line
phrase = 'hello \nscholar!\n'
print(phrase) 

# single backslash
phrase = "ada\\lovelace"
print(phrase)

#________________________________________________________________

# String Concatenation and Duplication
word_1 = "home"
word_2 = "work"

print(f"You can combine the words {word_1} and {word_2} \
to make the word {word_1+word_2}.")

print(f"These days, all I seem to do is {3*(word_1+word_2+' ')}.")

#________________________________________________________________

# Indexing/Slicing
      
name = "Ada Lovelace"
name[5] # "o"
name[20] # IndexError
name[0:3] # "Ada"
name[0:8] # "Ada Love"
name[0:8:2] # "AaLv"
name[-1] #e
print (f'I {name[4:8]} {name[0:3]} Community') # "I Love Ada Comminity"
      
#________________________________________________________________

# Debugging
      
# code block 1
# print('hello world!)
      
print('hello world!') # Debugging

# code block 2
# a = 3
# b = 4
# c = a*a + b***b
# print(c)

# Debugging
a = 3
b = 4
c = a*a + b**b #here
print(c)
      
# code block 3
# prnt("hello world!")

print("hello world!") # Debugging
      


