#Displays smallesy and then largest of three numbers

a = 7
b = 3
c = 2

if a < b and a < c:
    print(a, "is the smallest number")
elif b < a and b < c:
    print(b, "is the smallest number")
else:
    print(c, "is the smallest number")

if a > b and a > c:
    print(a, "is the largest number")
elif b > a and b > c:
    print(b, "is the largest number")
else:
    print(c, "is the largest number")

#When I changed the values of a, b, and c I got an output where "2" was both the largest and smallest number
#I got this error because I had two "if" statements instead of "elif" statements. This caused the program to check both conditions and print both outputs