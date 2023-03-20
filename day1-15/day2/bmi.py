height = float(input('insert height: '))
weight = int(input('insert weight: '))

bmi = weight/height**2
print('Your BMI is: ' + str(bmi))
#This is not rounding it
print('Your BMI as whole number is: ' + str(int(bmi)))
print('Your BMI as whole number rounded: ' + str(round(bmi)))