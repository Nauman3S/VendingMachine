import random, string
def getClientID():
    x = ''.join(random.choices(string.ascii_letters + string.digits, k=16))
    return x
print(getClientID())