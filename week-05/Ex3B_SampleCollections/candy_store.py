tuple_candy = ('Sour Patch Kids', 'Skittles', 'Gummy Bears')
tuple_flavor_options = ('Blueberry', 'Lemon', 'Watermelon')

candy_flavor_combos = set()
candy_flavor_combos.add(tuple_candy[0] + ': ' + tuple_flavor_options[0])
candy_flavor_combos.add(tuple_candy[0] + ': ' + tuple_flavor_options[1])
candy_flavor_combos.add(tuple_candy[0] + ': ' + tuple_flavor_options[2])
candy_flavor_combos.add(tuple_candy[1] + ': ' + tuple_flavor_options[0])
candy_flavor_combos.add(tuple_candy[1] + ': ' + tuple_flavor_options[1])
candy_flavor_combos.add(tuple_candy[1] + ': ' + tuple_flavor_options[2])
candy_flavor_combos.add(tuple_candy[2] + ': ' + tuple_flavor_options[0])
candy_flavor_combos.add(tuple_candy[2] + ': ' + tuple_flavor_options[1])
candy_flavor_combos.add(tuple_candy[2] + ': ' + tuple_flavor_options[2])

print(f"Today's candy options include: {candy_flavor_combos}")
#The candy flavor combos are randomized every time I run the code becuase it is in a set