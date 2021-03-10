# for-loop, range, conditional logic
# loop through 1-20 inclusive
#  for 4 and 13, print "x is unlucky"
# for even numbers, print "x is even"
# for odd numbers, print "x is odd"

for num in range(1, 21):
    if num == 4 or num == 13:
        print(f'{num} is unlucky')
    elif num % 2 == 0:
        print(f'{num} is even')
    else:
        print(f'{num} is odd')
