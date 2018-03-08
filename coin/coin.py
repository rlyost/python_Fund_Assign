
x = .23945593
y = .798839238
x_rounded = round(x)
# x_rounded will be rounded down to 0
y_rounded = round(y)
# y_rounded will be rounded up to 1

import random

def coin_toss(coins):
    head = 0
    tail = 0
    for x in range(coins+1):
        random_num = random.randint(1,2)
        if random_num == 1:
            head += 1
            print("Attempt #{}: Throwing a coin... It's a head! ... Got {} head(s) so far and {} tail(s) so far".format(x, head, tail))
        elif random_num == 2:
            tail += 1
            print("Attempt #{}: Throwing a coin... It's a tail! ... Got {} head(s) so far and {} tail(s) so far".format(x, head, tail))
coin_toss(5000)