starting_bank_balance = 5600
savings_goal = 10000
weekly_savings_amount_portion = 0.3
current_weekly_savings = 2600 * weekly_savings_amount_portion


while starting_bank_balance < savings_goal:
        starting_bank_balance += current_weekly_savings

if starting_bank_balance > savings_goal:
        starting_bank_balance = savings_goal

print("This week my balance increased to: " + str(starting_bank_balance))

print('Goal met! My current balance is: ' + str(starting_bank_balance))