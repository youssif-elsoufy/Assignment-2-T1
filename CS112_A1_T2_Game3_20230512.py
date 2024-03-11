# File: CS112_A1_T2_Game3_20230512.py
# Purpose: Subtract a square game. The player who remove last coin wins the game. Everyone
#          has to remove a square number from the number of coins the players decide.
# Author: Youssef Mohamed Mahmoud Mohamed
# ID: 20230512

import math


def perfect_square(number):
    # Take to check that the number is a perfect square
    return math.isqrt(number) ** 2 == number


def valid_input(coins_no):
    # Function to find all valid moves from the current pile.
    return [i for i in range(1, coins_no + 1) if perfect_square(i)]


coins_no = int(input('''Enter number of coins = '''))
print('Coins remaining =', coins_no)
while coins_no > 0:
    # Player 1 turn
    first_player = int(input('''Player 1, remove a square number of coins 
'''))
    # Check if the removed number is valid
    while first_player not in valid_input(coins_no):
        print('''Enter a valid square number
                                                ''')
        first_player = int(input('''Player 1, remove a square number of coins 
'''))
    # Update the number of coins after Player 1 remove
    coins_no = coins_no - first_player
    # Displaying the remaining and the removed coins number
    print('Coins removed =', first_player, '/', 'Coins remaining =', coins_no)
    # Check if Player 2 won
    if coins_no == 0:
        print('''Congratulation Player 1 won !''')
        break
    # Player 2 turn
    second_player = int(input('''Player 2, remove a square number of coins 
'''))
    # Check if the removed number is valid
    while second_player not in valid_input(coins_no):
        print('''Enter a valid square number
                                                    ''')
        second_player = int(input('''Player 2, remove a square number of coins 
'''))
    # Update the number of coins after Player 2 remove
    coins_no = coins_no - second_player
    # Displaying the remaining and the removed coins number
    print('Coins removed =', second_player, '/', 'Coins remaining =', coins_no)
    # Check if Player 2 won
    if coins_no == 0:
        print('''Congratulation Player 2 won !''')
        break
