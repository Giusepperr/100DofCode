import math

test_h= int(input('Height: '))
test_w= int(input('Width: '))

cov = 5

def paint_calc(height,width,coverage):
    print(f'you need {math.ceil(height*width/coverage)} cans of paint')
paint_calc(height=test_h,width=test_w,coverage=cov)