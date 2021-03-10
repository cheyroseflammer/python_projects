# ask for age
age = input('What is your age? ')

age = float(age)

# 18-21 wrist bad
if age >= 18 and age <= 21:
    print('You get a wrist band')
# 21+ drink, normal entry
elif age > 21:
    print('Normal entry')
# too young, sorry
else:
    print('too young sorry')
