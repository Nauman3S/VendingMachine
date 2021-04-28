import random
def Random_Alpha():

    l = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    s=""
    for i in range(0,16):
        s=s+l[random.randint(0,25)]
    return s
print(Random_Alpha())