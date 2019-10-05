#GC29
import random
numstudent = int(input("Input the number of students: "))
comlist = ["One of the best students I've had in my life","Needs to focus more in class","A very hard working student","Works very well with other students","Enthusiastic learner!","Commited in doing their best"]

for i in range(numstudent):
    newnum = random.randint(0,5)
    print("Student",i+1,":",comlist[newnum])