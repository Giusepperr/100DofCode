from replit import clear

bidders ={}
def add_bidder(name,bid):
    bidders[name]=bid
    
input('Welcome to the MF auction. Are you ready to bid?')

clear()
choice = ''
while choice != 'Y':
    name = input('Tell me the name mother fucker!')
    bid = int(input('Tell me the bid motherfucker'))
    add_bidder(name,bid)
    choice = input('Do you want to stop Y/whatever?')
    clear()
max = 0
for bidder in bidders:
    if max < bidders[bidder]:
        max = bidders[bidder]
        maxBidder = bidder
print(f'The winner is {maxBidder} with a bid of {max}')