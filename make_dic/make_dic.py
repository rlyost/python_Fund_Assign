name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane", "Oscar"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def make_dict(list1, list2):
    new_dict = {}
    new_list = []
    if len(list1) >= len(list2):
        new_list = zip(list1, list2)
    else:
        new_list = zip(list2, list1)        
    new_dict = dict(new_list)  
    return new_dict

print make_dict(name, favorite_animal)