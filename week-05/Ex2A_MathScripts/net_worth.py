#Basic Net Worth Formula
# 1. How do you calculate your net worth given your assets and debts?
# Assets: Cash, Ivestments, Vehicles, Property, Other Assets
# Debts: Mortgage, Loans, Credit Card Debt, Other Liabilities

assets = {
    "cash": 10000,
    "investments": 50000,
    "vehicles": 20000,
    "property": 100000,
    "other_assets": 10000
}
debts = {
    "mortgage": 80000,
    "loans": 20000,
    "credit_card_debt": 5000,
    "other_liabilities": 10000}

 #Total_Assets=Cash+Investments+Property+Other Assets
def calculate_total_assets(cash, investments, vehicles, property_value, other_assets):
    total_assets = cash + investments + vehicles + property_value + other_assets
    return total_assets

#Total_Debts=Mortgage+Loans+Credit Card Debt+Other Liabilities
def calculate_total_debts(mortgage, loans, credit_card_debt, other_liabilities):
    total_debts = mortgage + loans + credit_card_debt + other_liabilities
    return total_debts

#Net_Worth=Total_Assets-Total_Debts
def calculate_net_worth(assets, debts):
    net_worth = assets - debts
    return net_worth


total_assets = calculate_total_assets(
    assets["cash"],
    assets["investments"],
    assets["vehicles"],
    assets["property"],
    assets["other_assets"]
)

total_debts = calculate_total_debts(
    debts["mortgage"],
    debts["loans"],
    debts["credit_card_debt"],
    debts["other_liabilities"]
)

print(f"Your total assets are ${total_assets}")
#total_assets = calculate_total_assets(assets["cash"], assets["investments"], assets["vehicles"], assets["property"], assets["other_assets"])
print(f"Your total assets are ${total_assets}")
#total_debts = calculate_total_debts(debts["mortgage"], debts["loans"], debts["credit_card_debt"], debts["other_liabilities"])
print(f"Your total debts are ${total_debts}")
net_worth = calculate_net_worth(total_assets, total_debts)
#print(f"Your net worth is ${net_worth}")

