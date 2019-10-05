#GC23
#try = 1, conver = 2, pen = 3

team1 = input("What is Team 1's name?: ")
try1 = int(input("How many tries did team 1 score?: "))
conver1 = int(input("How many conversions did team 1 score: "))
pen1 = int(input("How many penalties did team 1 score?: "))
total1 = try1 + conver1*2 + pen1*3

team2 = input("What is Team 2's name?: ")
try2 = int(input("How many tries did team 2 score?: "))
conver2 = int(input("How many conversions did team 2 score: "))
pen2 = int(input("How many penalties did team 2 score?: "))
total2 = try2 + conver2*2 + pen2*3

print(team1,"scored a total of",total1,"points \nTries:",try1,"\nConversions:",conver1,"\nPenalties:",pen1)
print("")
print(team2,"scored a total of",total2,"points \nTries:",try2,"\nConversions:",conver2,"\nPenalties:",pen2)