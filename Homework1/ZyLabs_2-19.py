# Nicolas Campero
# 1856853

# Gather information from user of ingredients and servings amount
print('Enter amount of lemon juice (in cups):')
l_juice_cups = float(input())
print('Enter amount of water (in cups):')
water_cups = float(input())
print('Enter amount of agave nectar (in cups):')
agave_cups = float(input())
print('How many servings does this make?')
servings = int(input())

# output amount of ingredients for x amount of servings
print('\n', end='')
print('Lemonade ingredients - yields', '{:.2f}'.format(servings), 'servings')
print('{:.2f}'.format(l_juice_cups), 'cup(s) lemon juice')
print('{:.2f}'.format(water_cups), 'cup(s) water')
print('{:.2f}'.format(agave_cups), 'cup(s) agave nectar')

print('\n', end='')
print('How many servings would you like to make?')
servings_to_make = float(input())

# adjust amounts of each ingredient to match servings amount
print('\n', end='')
print('Lemonade ingredients - yields', '{:.2f}'.format(servings_to_make), 'servings')
multiple_of_servings = float(servings_to_make / servings)
lemon_after_servings = l_juice_cups * multiple_of_servings
water_after_servings = water_cups * multiple_of_servings
agave_after_servings = agave_cups * multiple_of_servings
print('{:.2f}'.format(lemon_after_servings), 'cup(s) lemon juice')
print('{:.2f}'.format(water_after_servings), 'cup(s) water')
print('{:.2f}'.format(agave_after_servings), 'cup(s) agave nectar')

# convert ingredient measurements from part 2 to gallons
lemon_gallons = lemon_after_servings / 16.00
water_gallons = water_after_servings / 16.00
agave_gallons = agave_after_servings / 16.00
print('\n', end='')
print('Lemonade ingredients- yields', '{:.2f}'.format(servings_to_make), 'servings')
print('{:.2f}'.format(lemon_gallons), 'gallon(s) lemon juice')
print('{:.2f}'.format(water_gallons), 'gallon(s) water')
print('{:.2f}'.format(agave_gallons), 'gallon(s) agave nectar')
