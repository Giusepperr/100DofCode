print('Wecolme to python pizza delivery!')

size = input("What size pizza do you want? S, M or L: ")

add_pepperoni = input("Do you want pepperoni? Y or N: ")

extra_cheese = input("Do you want extra cheese? Y or N: ")

cost = 0

if size == 'S':
    cost += 15
    if add_pepperoni == 'Y':
        cost += 2
elif size == 'M':
    cost += 20
    if add_pepperoni == 'Y':
        cost += 3
elif size == 'L':
    cost += 25
    if add_pepperoni == 'Y':
        cost += 3
else:
    print('The size was not correct')

if extra_cheese == 'Y':
    cost += 1

print(f'The cost of the pizza is {cost} Dorra')