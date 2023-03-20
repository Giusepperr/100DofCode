bill = float(input('What was the bill? in Dorra: '))
tip = int(input('How much tip do you want to give? '))
howManyPeople = int(input('How many people are there to split? '))

totalTip =  bill*(tip/100)
pay = round((totalTip + bill) / howManyPeople,2)

print(f'Each Person should pay: {pay} Dorra')
