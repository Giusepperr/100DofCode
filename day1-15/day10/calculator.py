from replit import clear

print('Welcome to the calculator')

def operation( x,y,op):
    """Perform an operation bewtween x and y. + - * / only ops available"""
    if op=='+':
        return x+y
    elif op=='-':
        return x-y
    elif op=='*':
        return x*y
    elif op=='/':
        return x/y

result = 'NA'
while True:
    if result == 'NA':
        first_operand = float(input('Provide Operand: '))
    else:
        first_operand = result
    operator = input('Choose the function + - / * : ')
    second_operand = float(input('Provide another operand: '))
    result = operation(first_operand, second_operand, operator)
    print(result)
    new_op = input('Do you want to perform a new op? y/n: ')

    if new_op.lower() == 'y':
        clear()
        result= 'NA'