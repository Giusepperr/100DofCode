import random

letters = ['a','b','c','d','e','f','g','h','i','l','m','n','o','p','q','r','s','t','u','v','z','x','y','k','j']
numbers = [1,2,3,4,5,6,7,8,9]
specialChars = ['@','#','$','%','^','&','*']

howManyLetters = int(input('How many letters should the pwd contain?'))
howManyNumbers = int(input('How many numbers should the pwd contain?'))
howManySpecialChar = int(input('How many SpecialChar should the pwd contain?'))

pwd = ''
for num in range(1,howManyLetters+1):
    pwd += letters[random.randint(0,len(letters)-1)]
for num in range(1,howManyNumbers+1):
    pwd += str(numbers[random.randint(0,len(numbers)-1)])
for num in range(1,howManySpecialChar+1):
    pwd += specialChars[random.randint(0,len(specialChars)-1)]

mem = ''
arrayString = list(pwd)
print(arrayString)
for num in range(1,len(arrayString)+1):
    curr = random.randint(0,len(arrayString)-1)
    next = random.randint(0,len(arrayString)-1)
    mem = arrayString[curr]
    arrayString[curr] = arrayString[next]
    arrayString[next] = mem
pwd = ''.join(arrayString)
print(pwd)

