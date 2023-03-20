#Data Types

#Strings are an array of char indexed from 0
'Hello'[0]

#Interger
12345456
#or instead of commas to visualize number better wow..
123_454_435

#Float

3.45

#Boolean

True
#or
False

#type(variable)
#the function type can be use to find out what type the var is
var = 2
print(type(var))

#str(var)
#str, float, int, function can be used to convert it to strings
var = str(var)
print(type(var))


#Challenge, take a number, and add the single values 39 = 12

number = input('insert number: ')
print(int(str(number)[0]) + int(str(number)[1]))

#Math Operators:
2+3
3-1
3*3
#division / always returns a float
3/4
#Round division is:
2//4
#power ops
4**3
#return op
4%3

#Math Operators are evalueted as PEMDAS Paranteses, Exponents, (Multiplication, Divisions), (Addintion, Subtraction)

# the function round() takes a number and the number of decimal places you want

#you can use += OP= to add the var the operation

var = 6
var += 2
print(var)

# F-String are composable strings so I can:
score = 0
height = 1.5
isWinning = True

print(f'The score is {score} and the height is {height} and you are winning {isWinning}')