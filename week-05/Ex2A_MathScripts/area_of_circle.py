#How do you calculate the area of a circle?
#Area of a Circle=π*Radius^2    

import math
radius = 13

def circle_area(radius):
    area = math.pi * (radius ** 2)
    return area

area = circle_area(radius)
print(f"The area of the circle with radius {radius} is {area:.2f}")