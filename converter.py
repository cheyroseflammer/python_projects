print('How many kilometers did you want to convert?')
kms = input()
miles = float(kms)/1.60934
rounded = round(miles, 2)
print(f'Your original {kms} kilometers is equal to {rounded} miles')
