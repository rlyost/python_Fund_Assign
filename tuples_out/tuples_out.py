# function input
my_dict = {
  "Speros": "(555) 555-5555",
  "Michael": "(999) 999-9999",
  "Jay": "(777) 777-7777"
}
#function output
# [("Speros", "(555) 555-5555"), ("Michael", "(999) 999-9999"), ("Jay", "(777) 777-7777")]

def tuple_out(dtot):
    newlist = []
    for x in dtot:
        tuple = ()
        tuple = (x,dtot[x])
        newlist.append(tuple)
    return newlist
print tuple_out(my_dict)

