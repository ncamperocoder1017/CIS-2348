# Nicolas Campero
# 1856853

# Get input from user for equation coefficients
x1 = int(input())
y1 = int(input())
num1 = int(input())
x2 = int(input())
y2 = int(input())
num2 = int(input())
check_equation = False

# Compare values of x and y from -10 to 10
for x in range(-10, 10, 1):
    for y in range(-10, 10, 1):
        if ((x1 * x) + (y1 * y) - num1 == 0) and ((x2 * x) + (y2 * y) - num2 == 0):
            check_equation = True
            print(x, y)
if check_equation is False:
    print("No solution")
