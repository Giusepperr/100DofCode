# A dictionary serves as finding values based on keys that are strings:

programming_dict = {
    "Bug":"Example",
    "Function":"Example"
}

print(programming_dict)
#to access the key:
programming_dict["Bug"] = "wHAT"
print(programming_dict["Bug"])

#In for loops the dict will go trough the keys not the values!

for key in programming_dict:
    print(key)
    print(f'You can still print the values as {programming_dict[key]}')

#Nesting means that you put a list or a dict in a dict

capitals ={
    "France":"Paris"
}

travel_log = {
    "France": ["Paris","lille","Dillon"],
    "example": {"what":"doyouwant"}
}