# Print top row
print "x",
for x in range(1, 13):
    if x < 12:
        print x,
    else:
        print x
# Print leftside first column
for i in range(1, 13):
    if i < 12:
        print i,
    else:
        print i 
# Prints all internal values of the multiplication table
    for y in range(1, 13):
        if y < 12:
            print (y * i),
        else:
            print (y * i) 

        