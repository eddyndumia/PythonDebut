# Number theoretic and representation functions from the math module

import math

x = 2.2
print(math.ceil(x))  # This function rounds up the float up to the nearest integer
print(math.floor(x))  # This is the opposite of .ceil() and will truncate the float to the nearest integer down

y = -2.2
z = 5
print(math.copysign(x, z))  # This function takes two parameters. The first parameter is the number you want to keep and
# the second is the sign you want to copy

a = -22
print(math.fabs(a))  # This function prints the absolute number of the parameter value passed

b = 4
print(math.factorial(b))  # This function will get the factorial of the number passed. For this instance 4 x 3 x 2 x 1

# sqrt -> will get the square root of an integers
c = 25
print(math.sqrt(c))

# gcd -> gets the greatest common divisor of two integers
d = 15
print(math.gcd(c,d))


# fsum -> gets the sum of a collection of integers

collection = [2, 4, 5, 8]
print(math.fsum(collection))

# lcm -> gets the least common multiple of two integers
print(math.lcm(d,c))
