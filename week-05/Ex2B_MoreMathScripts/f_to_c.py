#How do you convert a temperature from Fahrenheit to Celsius?
# The formula is: C = (F - 32) * 5/9

Fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
Celsius = (Fahrenheit - 32) * 5/9

print(f"The temperature in Celsius is {Celsius:.1f}°C")
