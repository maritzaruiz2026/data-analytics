#You are going to tile a room whose dimensions are length by width feet. There are twelve tiles per box, each 1 foot by 1 foot. How many boxes of tiles do you need? You can only buy full boxes, not a partial box.
#You also want to buy at least 10% more tiles than you need in order to handle chips, breakage, and mess-ups. How many total boxes will you buy?

import math

length = float(input("Enter the length of the room in feet: "))
width = float(input("Enter the width of the room in feet: "))
tiles_needed = (length * width) * 1.10  # Add 10% for breakage
boxes_needed = math.ceil(tiles_needed / 12)  # 12 tilesper box, round up to the nearest whole box using .ceil()
print(f"You need {int(boxes_needed)} boxes of tiles.")