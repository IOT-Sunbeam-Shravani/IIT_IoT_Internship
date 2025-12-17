import math
def area_circle(radius):
    return math.pi * radius *radius

def area_rectangle(length, breadth):
    return length * breadth

from ass5Q3 import area_circle, area_rectangle

r = float(input("Enter radius of circle:"))
l = float(input("Enter length of rectangle:"))
b = float(input("Enter breadths of rectangle:"))