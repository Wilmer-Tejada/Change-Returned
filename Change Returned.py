# Function that returns the least amount of coins to the user.

def num_coins(cents):

    coins = 0
    if cents <= 0:
        print('Please enter a positive number of cents.')

    while cents > 0:
        if cents >= 25:
            quarters = int(cents/25)
            cents = cents - quarters * 25
            coins = coins + quarters
        if cents >= 10:
            dimes = int(cents/10)
            cents = cents - dimes * 10
            coins = coins + dimes
        if cents >= 5:
            nickels = int(cents / 5)
            cents = cents - nickels * 5
            coins = coins + nickels
        if cents >= 1:
            pennies = int(cents)
            cents = cents - pennies
            coins = coins + pennies
    return coins
