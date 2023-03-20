#Today will do some random stuff and lists

#to import a module use:
import random

import my_mod

print(my_mod.pi)
random_int = random.randint(1,10)
print(random_int)

#Gens a random float number between 0.0 and 0.999 not includning 1
random_float = random.random()
print(random_float * 5)

#Lists in python are as the following indexed from 0

fruits = ['test', 'that','order']
print(fruits)
#you can count the indexed values positively or negatively: first and last:
print(fruits[0])
print(fruits[-1])
#there are a bunch of function that you can use with python list:
#append
#extend
#insert
#remove
#pop
#push

#you cab also use matrixs or lists of lists like so:
list = [1,2,3,4]
list2 = [5,6,7,8]
listOflist = [list,list2]
