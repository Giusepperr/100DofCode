print('Welcome to love Calc:')
name1 = input("What is your name?\n").lower()
name2 = input("What is your love name?\n").lower()

firstDigit = 0
firstDigit += name1.count('t')
firstDigit += name1.count('r')
firstDigit += name1.count('u')
firstDigit += name1.count('e')

secondDigit = name1.count("l")
secondDigit+= name1.count("o")
secondDigit+= name1.count("v")
secondDigit+= name2.count("e")

perc = int(str(firstDigit)+str(secondDigit))
print(perc)
if perc <=10 or perc>=90:
    print('you are alike mentos and coke')
elif perc <=40 or perc>=50:
    print(f'your score is {perc}%, its decent')
else:
    print(f'your score is {perc}')