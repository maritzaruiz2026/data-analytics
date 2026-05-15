###First function
#def display_mailing_label(name, address, city, state, zip):
#        print(f"""
#            {name}
#            {address} 
#            {city}, {state} {zip}
#""")

#display_mailing_label("Maritza Ruiz", "123 Milkyway Ave", "Chicago", "IL", "60625")
#display_mailing_label("Mariana Contreras", "125 Street Ave", "Chicago", "IL", "60907")

###Second function
#def add_numbers(*numbers):
#    total = sum(numbers)
#    joined_numbers = " + ".join(str(n) for n in numbers)
#    print(f'[{joined_numbers}] = {total}')

#add_numbers(2)
#add_numbers(7, 5)
#add_numbers(6, 3, 2)

##Third function
def display_receipt(total_due, amount_paid):
    change = amount_paid -  total_due 
    print(f'Total Due: ${total_due:.2f}\nAmount Paid: ${amount_paid:.2f}\n \nChange Due: ${change:.2f}\n\n')

display_receipt(79.50, 100)
display_receipt(79.50, 79.50)
display_receipt(79.50, 50)
