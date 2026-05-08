#How do you calculate the tip amount on a restaurant bill given the tip percentage?
#Tip Amount=Bill Amount*Tip Percentage

def calculate_tip_amount(bill_amount, tip_percentage):
    tip_amount = bill_amount * (tip_percentage / 100)
    return tip_amount


bill_amount = 73.20
tip_percentage = 15
tip_amount = calculate_tip_amount(bill_amount, tip_percentage)
print(f"The tip on a ${bill_amount:.2f} restaurant bill is ${tip_amount:.2f}")