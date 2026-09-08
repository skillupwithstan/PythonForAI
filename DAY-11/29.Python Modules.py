'''
# To find all available modules on the system
help('modules')

import random, math 
import os, sys

#help('random')
'''

# Random module
import random

x = 10
y = 50
print(random.randrange(x,y))

print("************************************")

# math module
import math
num1 = 23.81
num2 = 3
num3 = -27.01
print("Towards High Number,",num1,":",math.ceil(num1))
print("Towards Low Number,",num1,":",math.floor(num1))
print("The factorial of",num2,":", math.factorial(num2))
print("The absolute value of",num3,":",math.fabs(num3))
print("Number Truncation : ",math.trunc(num1))

print("Round-off Value : ",round(num1))

print("************************************")
