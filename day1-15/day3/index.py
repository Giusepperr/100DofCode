# This is about the flow of the software

condition = bool(input('did you insert anything?'))

if condition:
    print(f'the condition is {condition}')
else:
    print('the condition is not met')

#Logical Operators:
# > greater than or >=
# < lesser than or <=
# == equal
# != different

#you can nest if in each other:

if condition:
    if condition:
        print('another condition')
    else:
        print('what')
else:
    print('example')    

#You can use elif to give other conditions

if condition:
    print('this')
elif condition:
    print('another condi')
else:
    print('end of it')

# you can use multiple IF one after the other to check for condition
# even if the previous one was true

if condition:
    print('condition')
if condition:
    print('condition')
if condition:
    print('condition')

# Logical Operators

# And to get true both needs to be true
condition and condition
# OR to get true one of them needs to be true
condition or condition
# This commutes the validity of the condition
not condition

