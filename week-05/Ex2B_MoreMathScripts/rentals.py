#There are X people going on a tour. Charter vans seat 15 passengers each. Vans cost $250 per day to rent (including the driver’s pay). How many vans do you need? How much will it cost to rent vans? What is the cost if you split it per person?

import math

passengers = int(input("Enter the number of passengers going on the tour: "))
vans = math.ceil(passengers / 15)  #  15 passengers per van and round up for remaining passengers using .ceil()
total_cost = vans * 250
cost_per_passenger = total_cost / passengers
cost_per_passenger = round(cost_per_passenger, 2)

print(f"You need {int(vans)} vans.")
print(f"The total cost to rent vans is ${total_cost}.")
print(f"The cost per person is ${cost_per_passenger:.2f}.")

#For 38 tourists there would need to rent out 3 vans.
#My script said it would charge each person $19.74
#The vans were $750 total (for 3 vans)
#There was only $0.12 left over because the cost per person was rounded to the nearest tenth of a sent. The exact division of 750/38 is $19.736842105263158, which rounds to $19.74. 