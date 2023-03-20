# function can return values
# so far we saw how we can change existing value
#like this you can return values

def whatever(x,y):
    return x*y
print(whatever(3,4))

#We can use docstring to explain what the function does

def func(x,y):
    """Take a x and a y and make multiplication"""
    return x*y
# try to add the parameters you will see the docstring
func()