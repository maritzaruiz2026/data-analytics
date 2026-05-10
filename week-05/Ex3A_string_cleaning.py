name_1 = "PRIYA SHARMA" 
name_2 = "bob NGUYEN" 
name_3 = "LaTonya Williams" 
salary_1 = "$82,500" 
salary_2 = "$74,000" 

print(name_1.lower()) #priya sharma
print(name_2.lower()) #bob nguyen
print(name_3.lower()) #latonya williams

print(name_1.title()) #Priya Sharma
print(name_2.title()) #Bob Nguyen
print(name_3.title()) #LaTonya Williams

salary_1_cleaned = salary_1.replace('$', '')
print(salary_1_cleaned, type(salary_1_cleaned)) #82,500 <class 'str'>, after removing the $ they are now convirted as strings. To be able to perform math on them, we would need to remove the comma and convert them to integers or floats.
salary_2_cleaned = salary_2.replace('$', '')
print(salary_2_cleaned, type(salary_2_cleaned)) #74,000 <class 'str'>, same answer as above.

salary_1_math = int(salary_1.replace('$', '').replace(',', ''))
print(salary_1_math, type(salary_1_math)) #82500 <class 'int'>