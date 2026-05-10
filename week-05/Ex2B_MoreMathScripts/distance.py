#How do you calculate the distance between coordinates (x1, y1) and (x2, y2)?
#To calculate the square root in python, you can use the math.sqrt() function from the math module. The distance formula is: distance = math.sqrt((x2 - x1)^2 + (y2 - y1)^2)
import math

x1 = float(input("Enter the x-coordinate of the first point: "))
y1 = float(input("Enter the y-coordinate of the first point: "))
x2 = float(input("Enter the x-coordinate of the second point: "))
y2 = float(input("Enter the y-coordinate of the second point: "))

distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(f"The distance between the two points is {distance:.2f}")