def greet():
    print('Hello')
    print("How do you do?")

def greetWithName(name):
    print(f'Hello {name}')

print(greetWithName('luigi'))

#positional params just gets added one after the other:

def greetWithNameAndLocation(name,location):
    print(f"let's go brother {name} we go in {location}")

# to target the vars you can:
greetWithNameAndLocation(location='london',name='g')