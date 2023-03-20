studentScores = [80,65,60,54,78,74]

max= 0
for score in studentScores:
    if max<score:
        max = score

print(f'the max is: {max}')
