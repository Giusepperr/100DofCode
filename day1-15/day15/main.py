from functools import reduce

from coffe import model


def arrayToString(acc,next,deli =', '):
    acc += deli + next
    return acc

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
options = []
for keys in model:
    options.append(keys)
off = True
while(off):
    answer = ''
    while(answer not in options ):
        print(f'What would you like? {reduce(arrayToString,options)}')
        answer = input('')
    print('Insert the folliwing coins: '+ str(model[answer]["cost"])) 
    payment = float(input(' '))
    if(payment >= model[answer]["cost"]):
        print('your rest is: ' + str(payment - model[answer]["cost"]))
    else:
        print('not enough')
    off = False