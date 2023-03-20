def primeCheck(num):
    firstPrimes = [2,3,5,7,11]
    isPrime = True
    for i in range(2,num):
        if(num % i == 0):
            isPrime = False
    if(isPrime):
         print('its a prime number')
    else:
         print('its not a prime number')
          
number = int(input("input a number to test if is a prime number: "))

primeCheck(num=number)