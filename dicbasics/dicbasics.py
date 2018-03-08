# My name is Anna
# My age is 101
# My country of birth is The United States
# My favorite language is Python

me = {}
me["name"] = "Rick"
me["age"] = 51
me["country of birth"] = "the United States of America"
me["favorite language"] = "Python"

def pressdic(catch):
    for keys,values in catch.items():
        print("My {} is {}").format(keys,values)

pressdic(me)