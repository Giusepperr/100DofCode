import random

rockPaperScissor = ['Rock','Paper','Scissors']
choose = rockPaperScissor[int(input('Choose Rock as 0, Paper as 1, Scissors as 2\n'))]
computer = rockPaperScissor[random.randint(0,2)]

print(f'You Choose {choose}')
print(f'Computer Choose {computer}')
if (choose =='Rock' and computer =='Scissors') or (choose =='Paper' and computer =='Rock') or (choose =='Scissors' and computer =='Paper'):
    print('You win')
elif choose == computer:
    print('this is a draw')
else:
    print('you lose')