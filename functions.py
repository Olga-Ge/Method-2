

def greeting(name,sex):
    if sex == "m":
        prefix = "Mr"
    elif sex== "f":
        prefix = "Mrs"
    else:
        prefix =" "

    print("Hello {} {} how are you".format(prefix, name))
    print("My name is Olga")
    print("It is my pleasure to be working with you")

name_of= input ("please give me the name")
prefix = input ("sex")

greeting(name_of, prefix)
print("What if I want to greet someone else?")
greeting(prefix, name_of)