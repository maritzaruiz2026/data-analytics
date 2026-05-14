import random

products = ['Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam', 'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp', 'Surge Protector']

#print(f"Today's product of the day is {random.choice(products)}")

#print(f"The three products selected for the brief usability survey are: {random.sample(products, k = 3)}.")

#random.shuffle(products)
#print(products)

print(f'The daily transaction count for {random.choice(products)} is ${random.randint(50,300)}.')