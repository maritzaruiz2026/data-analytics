#How do you calculate the tip amount on a restaurant bill given the tip percentage?
#Tip Amount=Bill Amount*Tip Percentage


#bill_amount = 73.20
#tip_percentage = 15

bill_amount = float(input("How much was your bill? ")) 
print("Your bill amount is " + str(bill_amount))

tip_percentage = float(input("What percentage would you like to tip? ")) 
print("Your tip percentage is " + str(tip_percentage))

def calculate_tip_amount(bill_amount, tip_percentage):
    tip_amount = bill_amount * (tip_percentage / 100)
    return tip_amount

tip_amount = calculate_tip_amount(bill_amount, tip_percentage)
print(f"The tip on a ${bill_amount:.2f} restaurant bill is ${tip_amount:.2f}")

# When I originally ran my script I got an error saying could not convert string into float. I had the def section in the beggining of the script and moved it to the middle and it worked!