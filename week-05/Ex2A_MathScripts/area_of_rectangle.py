#The area of a rectangle is calculated by multiplying the length and width of the rectangle.
# Area = Length * Width

length = 12
width = 24

def rectangle_area(length, width):
    area = length * width
    return area

area = rectangle_area(length, width)
print(f"The area of the rectangle is {area}")
print(f"Side A is {length}")
print(f"Side B is {width}")
