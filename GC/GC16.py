#GC16

userinput = str(input("Please input your text: "))
if userinput.find("qwerty") == -1:
    print(userinput,"DOES NOT have 'qwerty' in their text")
else:
    print(userinput,"DOES have 'qwerty' in their text")