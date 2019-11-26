print("Recommended average calories needed (per day) = 2250 kcal")
caloriecount = 2250
foodlist = []
calorieslist = []
total = 0

while True:
    print("To finish, input 'end day'")
    foodname = str(input("Name of your food?: "))
    if foodname == 'end day':
        print("Total calories for today:",total)
        break
    else:
        while True:
            foodcalorie = int(input("Calories: "))
            if foodcalorie <0:
                print("Invalud input! Please try again")
            else:
                foodlist.append(foodname)
                calorieslist.append(foodcalorie)
                caloriecount = caloriecount - foodcalorie
                total = total + foodcalorie
                print("Recommended amount (left for today):",caloriecount)
                break
