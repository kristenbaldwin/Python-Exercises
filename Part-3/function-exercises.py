# Exercise 1

def hello(name):
    print("Hello {}".format(name))
hello(name = input("What is your name? "))

# Exercise 2

import matplotlib.pyplot as plot

def f(x):
    return x + 1

xs = list(range(-3, 4))
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()
plot.close()

# Exercise 3

import matplotlib.pyplot as plot

def f(x):
    return x * x
    
xs = list(range(-100,101))
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()
plot.close()

# Exercise 4

import matplotlib.pyplot as plot

def f(x):
    if x % 2 == 0:
        return -1
    else:
        return 1
    
xs = list(range(-5,6))
ys = []
for x in xs:
    ys.append(f(x))

plot.bar(xs, ys)
plot.show()
plot.close()

# Exercise 5

import matplotlib
import matplotlib.pyplot as plot
import math

def f(x):
    return math.sin(x)
    
xs = list(range(-5,6))
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()
plot.close()

# Exercise 6

import matplotlib
from numpy import arange
import matplotlib.pyplot as plot
import math

def f(x):
    return math.sin(x)
    
xs = arange(-5, 6, 0.1)
ys = []
for x in xs:
    ys.append(f(x))

plot.plot(xs, ys)
plot.show()
plot.close()

# Exercise 7

import matplotlib
import matplotlib.pyplot as plot

def fahrenheit(x):
    return float(x * 1.8 + 32)
    
xs = list(range(1, 16))
ys = []
for x in xs:
    ys.append(fahrenheit(x))

plot.plot(xs, ys)
plot.show()
plot.close()

# Exercise 8

play_again = input("Do you want to play again (Y or N)? ")

def again(x):
    if x == "Y":
        print("True")
        return True
    else:
        print("False")
        return False

again(play_again)

# Exercise 9

play_again = input("Do you want to play again (Y or N)? ")

while play_again != "Y" and play_again != "N":
        print("Invalid input.")
        play_again = input("Do you want to play again (Y or N)? ")

def again(x):
    if x == "Y":
        print("True")
        return True
    elif x == "N":
        print("False")
        return False
    
again(play_again)