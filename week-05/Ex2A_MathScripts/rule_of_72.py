# How long will it take a savings account worth X to double in value based on an interest rate of IR? (Hint: Look up the “rule of 72”) 
# The Rule of 72 is a quick, useful formula for estimating the number of years required to double an invested sum of money at a given annual fixed interest rate. By dividing 72 by the annual rate of return, you can calculate the approximate time it will take for your investment to double.
# Rule of 72: Time to Double = 72 / Annual Interest Rate 

#It would take 17.7 years (approx 18) for a savings account to double in value at an interest rate of 4% (72 / 4 = 18 years).


ir = 4
x = 5350
years = 18

#def calculate_time_to_double(ir):
#   time_to_double = 72 / ir
#   return time_to_double   
#time_to_double = calculate_time_to_double(ir)

def calculate_future_value(x, ir, years):
    future_value = x * (1 + (ir / 100)) ** years
    return future_value

future_value = calculate_future_value(x, ir, years)

formatted_future_value = format(future_value, ".2f")
formatted_years = format(years, ".1f")
formatted_interest_rate = format(ir/100, ".0%")

print(f"Your current savings is ${x}")
print(f"At a {formatted_interest_rate} interest rate, your savings account will be worth ${formatted_future_value} in {formatted_years} years")
