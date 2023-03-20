## How to create and manage Classes and create a quizz game with it.
#Don't forget that python is PascalCase first letter capitalized

#Create empty object:
class UserExample:
    pass

user_1 = UserExample()
# You can add an attribute simply:
user_1.username = 'test'

print(user_1.username)

#here how to create an object with initial values
#__init__ is called constructor and it's a piece of code always run when creating the func
# self it means that it references to the object created itself
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        #this is how to set a default value
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


        print('users being created')

# Constructor attributes are actually mandatory from now on.
user_1 = User('1','giusepperr')
user_2 = User('2','giusepperr')

user_1.follow(user_2)

print(user_1.following)
print(user_1.followers)
print(user_2.following)
print(user_2.followers)