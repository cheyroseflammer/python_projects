# Input 'Hey how are you?'
# repeat everything input until the user says 'stop copying me'

user_said = input('Hey how are you? ')

magic_word = 'stop copying me'

while user_said != magic_word:
    print(user_said)
    user_said = input()
print('FINE! YOU WIN')
