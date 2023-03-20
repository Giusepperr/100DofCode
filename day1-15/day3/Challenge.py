print("Welcome to the stupid game")
print("You need to find your love")

if input('Your love is blonde or brunette? \n') == 'brunette':
    print('You see two girl with dark hair in front of you')
    if input('You choose the girl that is "clever" or the one that is "fit"? \n') == 'fit':
        print('She looks at you wierdly')
        if input('You talk, kiss or leave her? \n') == 'leave':
            print('You win! the girl is following you now!')
        else:
            print('game over')
    else:
        print('game over')
else:
    print('game over')