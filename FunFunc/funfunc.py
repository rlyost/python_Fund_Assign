
def odd_even(start, end):
    for x in range(start, end+1):
        print "Number is ",x,".",
        if x % 2 == 0:
            print "This is an even number."
        else:
            print "This is an odd number."
odd_even(1, 2000)

a = [2,4,10,16]
def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] = arr[x] * num
    return arr
print multiply(a,5)
 
def layered_multiples(arr):
    new_array = []
    for y in range(len(arr)): #interate through values of a list
        temp = []
        for i in range(arr[y]): #iterates number of each list value
            temp.append(1)
        new_array.append(temp) #creates lists in the new list
    return new_array #returns new_array list of lists
x = layered_multiples(multiply([2,4,5],3)) #calls multiply function then the layered_multiples function
print x
# output
#>>>[[1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]]
