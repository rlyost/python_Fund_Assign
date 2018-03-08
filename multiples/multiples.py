#print all number from 0 to 1000 using a for loop
for count in range(1001):
    print(count)

#print every 5th number between 5 and 1000000
for count in range(5, 1000005, 5):
   print(count)

#sum all the numbers in a list and print result
a = [1, 2, 5, 10, 255, 3]
b = 0
for x in a:
    b = b + x
print(b)

#also easier
print sum(a)


#List average = 46
a = [1, 2, 5, 10, 255, 3]
print sum(a)/len(a)


