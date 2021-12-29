from math import pi, sqrt

def area(radius):
    return pi * radius ** 2

print(area(7))

def hypot(a, b):
    c2= a **2 + b **2
    c = sqrt(c2)
    return c

print(hypot(3, 4))