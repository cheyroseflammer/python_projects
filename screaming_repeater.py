# takes a num as user input
# prints "Clean your room" for every number user input specified

amount = input('How many times do I have to tell you? ')
amount = int(amount)

for time in range(amount):
    print('CLEAN YOUR ROOM!')
