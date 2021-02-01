# Nicolas Campero
# 1856853

# gather height and width of wall to calculate and output area of wall
print('Enter wall height (feet):')
wall_height = int(input())
print('Enter wall width (feet):')
wall_width = int(input())
wall_area = wall_height * wall_width
print('Wall area: {} square feet'.format(wall_area))

# find number of gallons of paint to cover wall
gallons_paint = float('{:.2f}'.format(wall_area / 350))
print('Paint needed: {} gallons'.format(gallons_paint))
cans_needed = round(gallons_paint)
print('Cans needed: {} can(s)'.format(cans_needed))

# print a new line
print('\n', end='')

# gather color of paint and cost of purchasing that color
print('Choose a color to paint the wall:')
color_paint = input()
colors = {
    'red': 35,
    'blue': 25,
    'green': 23
}
colors_gallons = cans_needed * colors[color_paint]
print('Cost of purchasing {} paint:'.format(color_paint), end=' $')
print(colors_gallons)
