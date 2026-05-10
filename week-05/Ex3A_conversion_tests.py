# Description: This script tests various numeric conversion techniques 
# Author: Maritza Ruiz


a = " 101.1 " 
b = '55' 
c = "402 Stevens"
d = 'Number 5 '

print(a)
a = ' 103.3 '
print(a, type(a)) 
#print(int(a)) #This caused an error because of the decimal point and the spaces, says invalid literal for int() with base 10:' 103.3 '
print(float(a)) 
print(int(float(a))) 
print(a.strip()) 


print(b)
b = '65'
print(b, type(b))
#print(int(b)) #This caused an error because of the decimal point, says invalid literal for int() with base 10: '65'
print(float(b)) 


print(c)
c = "710 Regan Street"
print(c, type(c))   
#print(int(c)) #This caused an error because of the non-numeric characters. Output was invalid literal for int() with base 10: "710 Regan Street"
#print(float(c)) #This caused an error because of the non-numeric characters. Output was invalid literal for float(): "710 Regan Street"
print(c) 
print(c[0:3])


print(d)
d = 'Number 25 '
print(d, type(d))   
#print(int(d)) #This caused an error because of the non-numeric characters. Output was invalid literal for int() with base 10: 'Number 25 '
#print(float(d)) #This caused an error because of the non-numeric characters. Output was invalid literal for float(): 'Number 25 '
print(d) 
print(d[7:9])
print(d.strip()) 