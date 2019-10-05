#GC32
#0 = confess #1 = silent
#0,0=5years,5years
#1,0=20years,released
#0,1=released,20years
#1,1=1year,1year

import random
while True:
    count = 1
    botdecision = random.randint(0,1)
    while True:
        print("Police: Are you going to confess? (Y/N)")
        userinput = input("You: ")
        if userinput in ['Y','y','Yes','yes']:
            userdecision = 0
            break
        elif userinput in ['N','n','No','no']:
            userdecision = 1
            break
        else:
            print("Error, please retry. ")

    if botdecision == 0 and userdecision == 0:
        print("You have both confessed, you will each recieve 5 years of jail time.")
    elif botdecision == 0 and userdecision == 1:
        print("You have not confessed but your buddy did, you will recieve 20 years of jail time.")
    elif botdecision == 1 and userdecision == 0:
        print("You have confessed but your buddy didnt, you will be released")
    else:
        print("You have both stayed silent, you will each recieve 1 year of jail time")
    print("")
    print("Game over!")
    print("--------------------------")

    playagain = input("Would you like to play again? (Y/N): ")
    if playagain in ['Y','y','yes','Yes']:
        count = count + 1
        print("")
    elif playagain in ['N','n','no','No']:
        count = 0
        break
    if count == 0:
        break