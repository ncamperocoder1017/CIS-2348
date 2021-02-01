# Nicolas Campero
# 1856853

print('Enter integer:')
user_num1 = int(input())  # get 1st integer input from user
print('You entered:', user_num1)
num1_squared = user_num1 ** 2  # square num1
num1_cubed = user_num1 ** 3  # cube num1

print(user_num1, 'squared is', num1_squared)
print('And', user_num1, 'cubed is', num1_cubed, '!!')

print('Enter another integer:')  # get 2nd integer input from user
user_num2 = int(input())
print(user_num2)
nums_sum = user_num1 + user_num2  # calculate sum of both inputs
nums_product = user_num1 * user_num2  # calculate product of both inputs
print('{} + {} is {}'.format(user_num1, user_num2, nums_sum))
print('{} * {} is {}'.format(user_num1, user_num2, nums_product))
