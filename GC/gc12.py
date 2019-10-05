#gc12
import time

siblingcount = int(input("How many siblings?: "))
x = 10
t = x/siblingcount

for x in range(siblingcount):
    print("Next person up! \n")
    time.sleep(t)
print("Time's up for everyone!")
