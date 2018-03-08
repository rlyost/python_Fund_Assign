
import random
random_num = random.random()
# the random function will return a floating point number, that is 0.0 <= random_num < 1.0
#or use...
random_num = random.randint(60,100)
print random_num

def grade_test(score):
    if score >= 90:
        print "Score:",score,"; Your grade is A"
    elif score >= 80:
        print "Score:",score,"; Your grade is B"
    elif score >= 70:
        print "Score:",score,"; Your grade is C"
    elif score >= 60:
        print "Score:",score,"; Your grade is D"
grade_test(random_num)