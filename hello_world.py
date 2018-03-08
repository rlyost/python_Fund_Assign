# print "Hello World!"
# x = "Hello Python"
# print x
# y = 42
# print y 

def multiply(arr,num):
    for x in range(len(arr)):
        arr[x] *= num
    return arr
a = [2,4,10,16]
b = multiply(a,5)
print b
# output:
# >>>[2,4,10,16]
