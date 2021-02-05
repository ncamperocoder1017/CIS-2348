# Nicolas Campero
# 1856853

# Ask user for current date
print('Birthday Calculator')
print('Enter the current day in the format MM/DD/YYYY')
current_month = int(input('Month: '))
current_day = int(input('Day: '))
current_year = int(input('Year: '))

# Ask user for birthday
print('Enter your birthday in the format MM/DD/YYYY')
bday_month = int(input('Month: '))
bday_day = int(input('Day: '))
bday_year = int(input('Year: '))

# Output user's age in years
current_age = current_year - bday_year
if current_month < bday_month:
    current_age -= 1
    print('You are {} years old.'.format(current_age))
else:
    print('You are {} years old.'.format(current_age))

if (bday_month == current_month) and (bday_day == current_day):
    print('Today is your birthday! Happy Birthday!')  # If current date is user's b-day, say "Happy Birthday!"
