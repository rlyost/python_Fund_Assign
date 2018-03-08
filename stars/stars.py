#Part I

x = [4, 6, 1, 3, 5, 7, 25]

def draw_stars(arr):
    for j in arr: #interate through list
        for i in range(j-1): #loop for value times-1 to print *
            print "*",
        print "*"
draw_stars(x)

#Part II

y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars2(arr):
    for j in arr: #interate through list
        if type(j) == str:
            for i in range(len(j)-1): #loop for value times-1 to print j[0]
                print j[0].lower(),
            print j[0].lower()
        else:
            for i in range(j-1): #loop for value times-1 to print *
                print "*",
            print "*"
draw_stars2(y)
