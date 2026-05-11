#Gross pay for pay_rate and hours_worked

pay_rate= float(input("Enter your pay rate: "))
hours_worked = float(input("Enter the number of hours worked: "))

over_time = hours_worked - 40
over_time_pay = over_time * (pay_rate * 1.5)
over_time_hours = (hours_worked - 40) > 0 and (hours_worked - 40) or 0
if hours_worked > 40:
    gross_pay = (pay_rate * 40) + over_time_pay
else:
    gross_pay = pay_rate * hours_worked

print("If you worked", hours_worked, "hours (with", over_time_hours, "hours of overtime), your gross pay is", gross_pay)