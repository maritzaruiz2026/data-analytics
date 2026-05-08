#How do you convert a temperature from Celsius to Fahrenheit?
# The formula is: F = (C * 9/5) + 32

Celsius = float(input("Enter the temperature in Celsius: "))
Fahrenheit = (Celsius * 9/5) + 32

print(f"The temperature in Fahrenheit is {Fahrenheit:.1f}°F")
