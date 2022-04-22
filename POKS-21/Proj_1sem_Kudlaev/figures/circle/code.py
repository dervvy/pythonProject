import math

default_radius = 5

def circle_perimeter(defrad=default_radius):
    return math.pi * defrad * 2

def circle_area(defrad=default_radius):
    return math.pi * (defrad ** 2)