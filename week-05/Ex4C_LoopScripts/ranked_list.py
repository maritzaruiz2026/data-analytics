favorite_foods = ['pizza', 'tacos', 'enchilladas', 'tampiquena', 'pasta']
for i, food in enumerate(favorite_foods, start=1):
    if i == 2:  
        print(f'{i}: {food} <- top pick!')
    else:
        print(f'{i}: {food}')

#added "continue" and it ended skipping 2, which is not what I wanted

for i, food in enumerate(reversed(favorite_foods), start=1):
    if i == 2:  
        print(f'{i}: {food} <- top pick!')
    else:
        print(f'{i}: {food}')
        #copied and pasted above but just added reversed()  