starting_bank_balance = 5600
savings_goal = 10000
weekly_savings_amount = 0.3 *2600    
treat_given = False

while starting_bank_balance < savings_goal:
    starting_bank_balance += weekly_savings_amount
    
    if starting_bank_balance > savings_goal:
        starting_bank_balance = savings_goal
    
    if starting_bank_balance >= savings_goal * 0.75 and not treat_given:
        starting_bank_balance = savings_goal * 0.75
        print('So close! After treating myself, my balance is up to ' + str(starting_bank_balance))
        treat_given = True
        continue

    print("This week my balance increased to: " + str(starting_bank_balance))

print('Goal met! My current balance is: ' + str(starting_bank_balance))

#I kept getting an output of 10000.0 and I was confused 
#I entered my code into Copilot and realized my indentation was off! Corrected it and now it works 
#While alterating my script to add the "*0.75" function in between my loop I kept getting erros and I realized I had to add a "continue" statement to skip the rest of the loop and avoid the error.
#Even when doing so I kept getting repetitive outputs of "So close! After treating myself, my balance is up to 7500.0" and I realized I had to add a boolean variable to make sure the treat was only given once.
#The boolean function was something Copilot pointed out to add to correct the error, I attempted break originaly and it failed
#This was by far the hardest script I have faced yet 