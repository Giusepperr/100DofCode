import random

names = input('Provide everybody names to see who pays:\n')
ArrayNames = names.split(',')

length = len(ArrayNames)

print(f'the bill will be paid by {ArrayNames[random.randint(0,length-1)]}')
print(f'the tip will be paid by {random.choice(ArrayNames)}')