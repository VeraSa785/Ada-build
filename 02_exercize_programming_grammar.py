# Practice Problems
# 1. Variables and Assignment

# problem 1.1
x = 5
# what value does x now hold?
print(x)

# problem 1.2
z = "Hello"
# what value does z now hold?
print(z)

# problem 1.3
a = 5
b = 3.2
c = a + b
# what values does c now hold?
print(c)

# problem 1.4
var1 = "lawl"
var2 = "brb"
# what value does var2 now hold?
print(var2)

# problem 1.5
e = 6 + 3
# what values does e now hold?
print(e)

# problem 1.6
f = 3.5
f = f + 2
# what value does f now hold?
print(f)

# problem 1.7
poodle = 4
pitbull = 3
# what value does boxer now hold?
#TraceBack: boxer is not definite

# problem 1.8
h = 5
h = h + h
# what values does h now hold?
print(h)

# problem 1.9
j = 1
k = 2
m = 3
n = j + k + m
# what value does n now hold?
print(n)

# problem 1.10
l = "moo"
q = "quack"
l  = q
# what value does l now hold?
print(l)

# problem 1.11
r = "moo"
s = "quack"
t = "woof"
r = t
# what value does r now hold?
print(r)

# problem 1.12
u = 5
u = u * 2
u = u * 2
u = u * 2
# what value does u now hold?
print(u)

# problem 1.13
v = "b"
z = "a"
# what value does v now hold?
print(v)

# problem 1.14
aa = 3234
bb = 2398
cc = 1
dd = (aa + bb) / cc
# what value does dd now hold?
# ZeroDivisionError: division by zero

# problem 1.15
yy = 7
zz = yy % 2
# what value does zz now hold?
print(zz)

# problem 1.16
ee = 12
ff = ee % 4
# what value does ff now hold?
print(ff)

# problem 1.17
zz = 17
hh = zz % 3
# what value does hh now hold?
print(hh)

#________________________________________________________________________________________

# Operators
# Consider the following variable assignments and then fill in the table.

d = 10
e = 5.0
f = 2
g = 11.0
h = 3
i = 1.5

print((type(d+e)),d+e)
print((type(f+h)),f+h)
print((type(g+h)),g+h)
print((type(d-f)),d-f)
print((type(g-e)),g-e)
print(type((h+i)-f),(h+i)-f)
print(type((d-f)+e),(d-f)+e)
print((type(d*f)),d*f)
print((type(g*i)),g*i)
print((type(f*g)),f*g)
print((type(d/f)),d/f)
print((type(d/e)),d/e)
print((type(e/f)),e/f)
print(type((g*f)/f),(g*f)/f)
print(type((d/f)*e),(d/f)*e)
print(type(21/5),21/5)
print(type(14/5),14/5)
print(type(10%3),10%3)
print(type(20%2),20%2)
print(type(4%5),4%5)
print(type(8%1),8%1)

#________________________________________________________________________________________

# Strings
# Determine the results for each of the following problems on your own and then check your answer using the code block below.

# problem 3.1
my_string = "I love Seattle"
my_string[7]
 
# problem 3.2
my_string = "I love Seattle"
my_string[2:4]
 
# problem 3.3
my_string = "Ada"
my_string += " Lovelace"
 
# problem 3.4
my_string = "Ada"
my_string += " codes" + " it!"
 
# problem 3.5
my_string = "Ada"
(my_string + " likes to code")[4:9]
 
# problem 3.6
my_string = "Hello world"
"Goodbye " + my_string[6:11] + "!"
 
# problem 3.7
my_string = "Hello world!"
my_string[0:5] + ", goodbye!"
 
# problem 3.8
my_string = "Hello world!"
my_string[:1] + "i" + "!"
 
# problem 3.9
my_string = "I love Python"
my_string[7:13] + my_string[2:6] + my_string[0]
 
# problem 3.10
my_string = "I love Python"
"P" + my_string[8:13] + " rocks!"
 
# problem 3.11
my_string = "I love Python"
my_string[2:6] + my_string[7:13] + my_string[2:6]
