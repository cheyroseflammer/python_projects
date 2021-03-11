# Print ('\U0001f600')
# 1-10 times on a separate line each
# Use and for and a while loop
# take advantage of the fact that you can multiply a string by a number and print it out
#
##
###
####
#####
######
########
#########
##########


# while loop

num = 0
while num < 10:
    num += 1
    print(num * '\U0001f600')


# for loop

for num in range(1, 11):
    print(num * '\U0001f600')

# using a for and while loop

for num in range(1, 11):
    count = 1
    emoji = ''
    while count <= num:
        emoji += '\U0001f600'
        count += 1
    print(emoji)
