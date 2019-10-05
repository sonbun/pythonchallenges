#GC26
import random
import string

def randomString(stringLength):
    letters = string.ascii_letters
    return ''.join(random.choice(letters) for x in range(stringLength))
newword = randomString(8)
print("Please type in",newword)
typeword = input(":")
if newword == typeword:
    print("Success")
else:
    print("Failed")