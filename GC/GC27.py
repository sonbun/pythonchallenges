#GC27
for x in range(1,21):
    y = 21 - x
    if y%3==0 and not y%5==0:
        print("Fizz")
    elif y%5==0 and not y%3==0:
        print("Buzz")
    elif y%3==0 and y%5==0:
        print("FizzBuzz")
    else:
        print(y)