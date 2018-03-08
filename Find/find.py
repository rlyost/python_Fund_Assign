# input
word_list = ['hello','world','my','name','is','Anna']
char = 'o'
# output
#new_list = ['hello','world']

new_list = []
for x in word_list:
    for i in x:
        if i == char:
            new_list.append(x)
print new_list      
