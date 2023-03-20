import random

#We are now just doing challenges
words = ['test','whatever','blaalba']
wordChoose =random.choice(words)

emptyArray = []
for num in range(len(wordChoose)):
    emptyArray.append('_')
print(emptyArray)
life = 0
while life<5 and  '_' in emptyArray:
    print(f'you have {5-life} left')
    inp = input('provide a letter: ').lower()
    if inp in wordChoose:
        index = 0
        for letter in wordChoose:
            if(letter == inp):
                emptyArray[index] = letter
            index+=1
    else:
        life+=1
    print(emptyArray)
if life >= 5:
    print('You lost')
else:
    print('You win')