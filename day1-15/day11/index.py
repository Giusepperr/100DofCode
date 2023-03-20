#lets see what we do today!
#Awesome balckjack gaaaamess
import json
import random


class card:
    def __init__(self,type,value,seed):
        self.type = type
        self.value = value
        self.seed = seed
    def __str__(self):
        return f'Card: type: {self.type}, value: {self.value}, seed: {self.seed}'
    def __repr__(self):
        return f'Card: type: {self.type}, value: {self.value}, seed: {self.seed}'
    def returnCard(self):
        return {'type':self.type, 'value':self.value,'seed':self.seed}

class deck:
    seeds = ['d','c','b','a']
    types = ['A','1','2','3','4','5','6','7','8','9','10','J','Q','K']
    values = [11,1,2,3,4,5,6,7,8,9,10,10,10,10]
    def createDeck(self):
        deck = []
        for seed in self.seeds:
            for index in range(0,13):
                deck.append(card(self.types[index],self.values[index],seed))
        return deck
    def shuffle(deck):
        random.shuffle(deck)
        return deck
    def initialDrawUser(deck):
        userHand = []
        dealerHand = []
        for i in range(0,2):
            userHand.append(deck.pop(0))
        for i in range(0,2):
            dealerHand.append(deck.pop(0))
        return {'dealerHand':dealerHand,'userHand':userHand}
    def totalHandValue(hand):
        acc = 0
        aces = 0
        for card in hand:
            acc += card.value
            if(card.value == 11):
                aces+=1
        if(acc > 21 and aces>0):
            acc -= 10
            
        return acc
    def drawACard(deck,hand):
        hand.append(deck.pop(0))
        return hand


deckDef = deck()
go = True
print('Welcome to the blackJack game boys and girls')
while go:
    print('Creating the Deck')
    deckInUse= deckDef.createDeck()
    print('Shuffle The deck')
    deckInUse = deck.shuffle(deckInUse)
    cardsDrawn = deck.initialDrawUser(deckInUse)
    dealerHand = cardsDrawn['dealerHand']
    dealerUncovered = dealerHand[1]
        
    userHand =cardsDrawn['userHand']
    againCard = 'y'
    dealerPlay = 'y'
    while(againCard == 'y'):
        print(f'The Dealer uncoveder card is: {dealerUncovered} \n Your cards are: {userHand}, your total is: {deck.totalHandValue(userHand)}!!')
        againCard = input('Do you want a card? y/n: ')
        if(againCard == 'y'):
            userHand = deck.drawACard(deckInUse,userHand)
            print(f'You have drawn: {userHand[-1]}')
        if(deck.totalHandValue(userHand)>21):
            print(f'your total is above 21, its {deck.totalHandValue(userHand)} you lose!')
            dealerPlay = 'n'
            againCard = 'n'
        elif(deck.totalHandValue(userHand)==21):
            print('you made 21 the Max')
            againCard = 'n'
    if(dealerPlay == 'y'):
        while(deck.totalHandValue(dealerHand)<17):
            dealerHand = deck.drawACard(deckInUse,dealerHand)
        if(deck.totalHandValue(dealerHand)>21):
            print('Dealer Loses his total is more than 21')
        elif(deck.totalHandValue(dealerHand)>deck.totalHandValue(userHand)):
            print(f'Dealer Wins {deck.totalHandValue(dealerHand)} against your {deck.totalHandValue(userHand)}')
        elif(deck.totalHandValue(dealerHand)==deck.totalHandValue(userHand)):
            print('Its a draw!')
        else:
            print(f'You Win {deck.totalHandValue(userHand)} against your {deck.totalHandValue(dealerHand)}')
    if(input('Do you want to play again?')!='y'):
        go = False
        


