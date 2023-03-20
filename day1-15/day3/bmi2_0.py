height = float(input('What is your height in m: '))
weight = float(input('What is your weight in kg: '))

bmi = round(weight/height**2,1)
print(f'your bmi is {bmi}')
if bmi <18.5:
    print('you are underweight')
elif bmi <25:
    print('your weight is normal')
elif bmi <30:
    print('you are overweight')
elif bmi <35:
    print('you are obese')
else:
    print('you are clinically obese')