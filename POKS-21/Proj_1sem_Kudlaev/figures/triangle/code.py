import math

a, b, c = 7, 2, 8


def triangle_perimeter(a, b, c):
    return a + b + c


def triangle_area(a, b, c):
    p = (a + b + c)/2
    return math.sqrt(p * (p - a) * (p - b) * (p - c))