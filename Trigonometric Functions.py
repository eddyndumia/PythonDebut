# These are functions to do with trigonometry. E.g Sin, Cos, Tan, Hypotenuse etc
import math

a = math.cos(90)  # This returns the cosine of x/parameter
print(a)

b = math.sin(90)  # This returns the sine of x/parameter specified
print(b)

c = math.tan(90)  # This returns  the tangent of x/parameter specified
print(c)

d = math.asin(0)  # This function returns the arc sine of the parameter value
print(d)

e = math.atan(0)  # Returns the arc tangent of a value specified
print(e)

f = math.acos(0)  # This returns the arc cosine of a parameter passed
print(f)

# trigonometric // triangle perpendicular height and base length below

height = 3
base = 4

# to find the hypotenuse use math.hypotenuse()
hypotenuse = math.hypot(height, base)
print(hypotenuse)

# get the distance between two points

point = [2, 1]
point2 = [4, 2]

distance = math.dist(point, point2)
print(distance)



