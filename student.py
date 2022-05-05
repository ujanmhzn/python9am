x=1
num_of_std=int(input("enter the number od student:"))
student_marks=[]
while x<=num_of_std:
    for i in range(1):
        print(f"================Student no: {x}===========")
        nep =int(input("enter the marks of nep"))
        eng = int(input("enter the marks of eng"))
        maths = int(input("enter the marks of maths"))
        social= int(input("enter the marks of social"))
        com = int(input("enter the marks of com"))
        mark=[nep,eng,maths,social,com]
        student_marks.append(mark)



    x+=1
for mark in student_marks:
    total=0
    for mr in mark:
        total+=mr
    pre=total/5
    division=""
    if pre>34 and pre<=45:
        division += "third"
    elif pre>45 and pre<=65:
        division+="second"
    elif pre>65 and pre<=75:
        division+="first"
    elif pre>75 and pre<=85:
        division+="distinsion"
    else:
        division+="fail"
        print(f"student number:{x}pre:{pre}div:{division}")
    x+=1


