# Description: This script tests various numeric 
#   conversion techniques 
# Author: Sam Q. Newprogrammer


a = " 101.1 " 
b = '55' 
c = "402 Stevens" 
d = 'Number 5 '

#print(int(a)) #This caused an error because of the decimal point and the spaces, says invalid literal for int() with base 10:' 101.1 '
#print(float(a)) #This worked and converted the string to a float, ignoring the spaces. Output was 101.1
#print(int(float(a))) #This worked and converted the string to an integer, ignoring the spaces and the decimal point. Output was 101
#print(int(b)) #This worked and converted the string to an integer. Got 55 as output
#print(float(b)) #This worked and converted the string to a float. Output was 55.0
#print(int(c)) #This caused an error because of the non-numeric characters. Output was invalid literal for int() with base 10: '402 Stevens'
#print(float(c)) #This caused an error because of the non-numeric characters. Output was invalid literal for float(): '402 Stevens' 
#print(int(d)) #This caused an error because of the non-numeric characters. Output was invalid literal for int() with base 10: 'Number 5 '
#print(float(d)) #This caused an error because of the non-numeric characters. Output was invalid literal for float(): 'Number 5 '

