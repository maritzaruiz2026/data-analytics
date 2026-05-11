#will calculate federal tax based on the values of annual gross income (a number) and a filing status (‘single’ or ‘joint’).

pay_rate= float(input("Enter your pay rate: "))
weekly_hours_worked = float(input("Enter the number of hours you work per week: "))
filer_status = input("Enter your filing status (single or joint): ").lower()

over_time = weekly_hours_worked - 40
over_time_pay = over_time * (pay_rate * 1.5)
over_time_hours = (weekly_hours_worked - 40) > 0 and (weekly_hours_worked - 40) or 0
if weekly_hours_worked > 40:
    gross_pay = (pay_rate * 40) + over_time_pay
    yearly_gross_pay = ((pay_rate * 40) + over_time_pay) * 52
else:        
    gross_pay = pay_rate * weekly_hours_worked
    yearly_gross_pay = pay_rate * weekly_hours_worked * 52  

if filer_status == "single":
    if yearly_gross_pay < 12000:
        taxes_owed = 0.05 * yearly_gross_pay
    elif yearly_gross_pay < 25000:
        taxes_owed = 0.10 * yearly_gross_pay
    elif yearly_gross_pay < 75000:
        taxes_owed = 0.15 * yearly_gross_pay
    else:
        taxes_owed = 0.20 * yearly_gross_pay

elif filer_status == "joint":
    if yearly_gross_pay < 12000:
        taxes_owed = 0.00 * yearly_gross_pay
    elif yearly_gross_pay < 25000:
        taxes_owed = 0.06 * yearly_gross_pay
    elif yearly_gross_pay < 75000:
        taxes_owed = 0.11 * yearly_gross_pay
    else:
        taxes_owed = 0.20 * yearly_gross_pay

print("If you worked", weekly_hours_worked, "hours weekly (with", over_time_hours, "hours of overtime), with an hourly pay rate of $", pay_rate, ", your weekly gross pay is $", gross_pay)
print("If you are filing as", filer_status, "and your yearly gross pay is $", yearly_gross_pay, "then you owe $", taxes_owed, "in taxes.")
print("Your weekly taxes withholdings are $", taxes_owed / 52, "which is", (taxes_owed / 52) / gross_pay * 100, "% of your weekly gross pay.")
print("Your yearly gross pay is $", yearly_gross_pay)
print("Your Net Pay is $", yearly_gross_pay - taxes_owed)