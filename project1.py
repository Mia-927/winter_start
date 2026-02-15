# student managment
#これから課題3
#menu
dic=[]
print("Main menu",'1.student add','2.display student','3.Search student','4.Exit',sep='    ')

#平均、合計出す
def advrage(students):
    alls=n=0
    for student in students:
        for value in student.values():
            alls += value
            n +=1        
    average=alls/ n #len(dic)
    print(alls,average)
    return  average

#学生データを“探す"
def st_search(students,find):
    n=0
    find =False
    for student in students:
        for key,value in student.items():
            if key==find:
                print(key,'s score is',value)
                break
            else:
              
                continue
    print("student not found")

def st_pass(students):
    pas=[]
    for student in students:
        for key,value in student.items():
            if value>= 60:
                pas.append(student)
            else:
                continue
    return pas

"""found = False

for student in students:
    if found==1:
        print
        found = True
        break

if found == False:
    見つからなかったと表示
"""

while 1:
    while 1:
        inputs=int(input('Select menu: '))
        if inputs==1:
            name=input("input the students name")
            score=int(input("input the students score"))
            st={name:score}
            dic.append(st)
            advrage(dic)
    
        elif inputs==2:
            print(dic)
            a=st_pass(dic)
            print(a)

        elif inputs==3:
            find=input("Enter the exact name: ")
            st_search(dic,find)
             
        elif inputs==4:
            print("Exit")
            break
    #except:
   #     print("invalid selection")
        
    
