year = int(input('Provide a year to test if is a leap year: '))

if year % 100 == 0:
    if year % 400 == 0:
        print('this is a leap year')
    else:
        print('this is not a leap year')
elif year % 4 == 0:
    if year % 100 != 0:
        print('this is a leap year')
    else:
        print('this is not a leap year')
else:
    print('this is not a leap year')

#another same way is:

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print('this is a leap year')
        else:
            print('this aint a leap year')
    else:
        print('this is a leap year')
else:
    print('this aint a leap year')