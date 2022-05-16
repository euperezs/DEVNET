"""Intro to Python - Part 1 - Hands-On Exercise."""


import math
import random
from unittest import result


# TODO: Write a print statement that displays both the type and value of `pi`
pi = math.pi

print (pi)
print (type(pi))
print ("""
Fin del primer TODO

_________________________________________

""")

# TODO: Write a conditional to print out if `i` is less than or greater than 50
i = random.randint(0, 100)

if i > 50:
    print ("'i' is greater than 50")
    print ("'i' value is: ", i)
elif i < 50:
    print ("'i' is less than 50")
    print ("'i' value is: ", i)
else:
    print ("'i' equals 50")
    print ("'i' value is: ", i)

print ("""
Fin del segundo TODO

_________________________________________

""")


# TODO: Write a conditional that prints the color of the picked fruit
picked_fruit = random.choice(['orange', 'strawberry', 'banana'])

if picked_fruit == "orange":
    print ("picked fruit is: " + picked_fruit)
    print ("fruit color is orange")
elif picked_fruit == "strawberry":
    print ("picked fruit is: " + picked_fruit)
    print ("fruit color is red")
elif picked_fruit == "banana":
    print ("picked fruit is: " + picked_fruit)
    print ("fruit color is yellow")

print ("""
Fin del tercer TODO

_________________________________________

""")

# TODO: Write a function that multiplies two numbers and returns the result
# Define the function here.
def multiplicacion(a, b):
    resultado = a * b
    return resultado

# TODO: Now call the function a few times to calculate the following answers

print("12 x 96 =", multiplicacion(12, 96))

print("48 x 17 =", multiplicacion(48, 17))

print("196523 x 87323 =", multiplicacion(196523, 87323))

print ("""
Fin del quinto TODO

_________________________________________

""")