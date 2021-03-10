import random

print('Rock...')
print('Paper...')
print('Scissors...')

player1 = input('Enter a your choice: ')

choice_list = ['rock', 'paper', 'scissors']

computerPlayer = random.choice(choice_list)


if player1 == computerPlayer:
    print(
        f'Its a tie! Player 1 picked {player1} and computer picked {computerPlayer}!')
elif player1 == 'rock':
    if computerPlayer == 'scissors':
        print('Player 1 wins, computer played scissors.')
    elif computerPlayer == 'paper':
        print('Computer wins, computer played paper.')
elif player1 == 'paper':
    if computerPlayer == 'rock':
        print('Player 1 wins, computer played rock.')
    elif computerPlayer == 'scissors':
        print('Computer wins, computer played scissors.')
elif player1 == 'scissors':
    if computerPlayer == 'rock':
        print('Computer wins, computer played rock.')
    elif computerPlayer == 'paper':
        print('Player 1 wins, computer played paper.')
else:
    print('Oops, something went wrong.')
