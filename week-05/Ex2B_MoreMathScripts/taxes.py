#Federal taxes are 23% of your salary every month. You make X amount of money. How much is withheld for taxes?

Salary = float(input("Enter your monthly salary: "))
TaxWithholding = Salary * 23/100

print(f"The amount withheld for taxes is ${round(TaxWithholding, 2)}")