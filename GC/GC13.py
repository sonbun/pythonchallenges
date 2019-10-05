#GC13

isbn = int(input("What is the ISBN Number?: "))
digit1 = [int(x) for x in str(isbn)]

odd = digit1[0]+digit1[2]+digit1[4]+digit1[6]+digit1[8]+digit1[10]
even = digit1[1]+digit1[3]+digit1[5]+digit1[7]+digit1[9]+digit1[11]
result1 = even * 3
result2 = (result1+odd) % 10
if result2 > 0:
    result3 = 10- result2
    digit1.append(result3)
for x in digit1:
    print(x, end='')