#write a Python program which accepts the radius of a circle from the user and computes area.
import math

r = float(input("Input the radius of the circle: "))
area = math.pi * r ** 2
print(f"The area of the circle with radius {r} is: {area}")


