from random import randint

from data import data

print('Welcome to higher or lower game')
again = True
score = 0

dataLen = len(data)
randomOne = data[randint(0,dataLen)]
while(again):

    randomTwo = data[randint(0,dataLen)]
    print(f'Who has more insta follower between {randomOne["name"]} or {randomTwo["name"]}?')
    choice = input(f'A for {randomOne["name"]} or B for {randomTwo["name"]}: ')
    if(choice == 'A'):
        if(randomOne["follower_count"] > randomTwo["follower_count"]):
            score +=1
        else:
            again = False
    else:
        if(randomOne["follower_count"] < randomTwo["follower_count"]):
            score+=1
        else:
            again = False
    randomOne = randomTwo

print(f'You Lose, your score is {score}: ')    