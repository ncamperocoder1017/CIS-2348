# Nicolas Campero
# 1856853

# def function exact_change
def exact_change(user_total):
    dollars = user_total // 100  # converts to dollar amount
    user_total %= 100  # gets the remainder after the conversion to dollars
    quarters = user_total // 25  # converts to quarter amount
    user_total %= 25  # gets the remainder after the  conversion to quarters
    dimes = user_total // 10  # converts  to dime amount
    user_total %= 10  # gets the remainder after the conversion
    nickels = user_total // 5  # converts to nickel amount
    user_total %= 5  # gets the remainder after the conversion
    pennies = user_total
    return dollars, quarters, dimes, nickels, pennies


if __name__ == '__main__':
    inputval = int(input())
    dollars_new, quarters_new, dimes_new, nickels_new, pennies_new = exact_change(inputval)

    # give output from if and else statements; individual vs. plural distinction
    if dollars_new > 1:
        print('{} dollars'.format(dollars_new))
    elif dollars_new == 1:
        print('1 dollar')

    if quarters_new > 1:
        print('{} quarters'.format(quarters_new))
    elif quarters_new == 1:
        print('1 quarter')

    if dimes_new > 1:
        print('{} dimes'.format(dimes_new))
    elif dimes_new == 1:
        print('1 dime')

    if nickels_new > 1:
        print('{} nickels'.format(nickels_new))
    elif nickels_new == 1:
        print('1 nickel')

    if pennies_new > 1:
        print('{} pennies'.format(pennies_new))
    elif pennies_new == 1:
        print('1 penny')

    if inputval <= 0:
        print('no change')
