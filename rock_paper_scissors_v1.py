# rock, paper, scissors
# (enter Player 1 choice): rock
# (enter Player 2 choice): paper
# shoot!
# player2 wins!

print('Rock...')
print('Paper...')
print('Scissors...')

player1 = input('Player 1, enter a choice: ')
player2 = input('Player 2 enter a choice: ')

if player1 == 'rock' and player2 == 'scissors':
    print('Player 1 wins!')
elif player1 == 'scissors' and player2 == 'rock':
    print('Player 2 wins')
elif player1 == 'paper' and player2 == 'rock':
    print('Player 1 wins')
elif player1 == 'rock' and player2 == 'paper':
    print('Player 2 wins')
elif player1 == 'scissors' and player2 == 'paper':
    print('Player 1 wins')
else:
    print('Player 2 wins')
