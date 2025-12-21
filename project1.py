# student managment

#student
dic={}
alls=0
average=0
print("Main menu",'1.student add','2.display student','3.Exit',sep='    ')

def advrage(st,alls):
    for key,value in st.items():
        alls += value
        average=alls/len(st)
    print(alls,average)


while 1:
    try:
        inputs=int(input('Select menu: '))
        if inputs==1:
            name=input("input the students name")
            score=int(input("input the students score"))
            st={name:score}
            dic=st
            advrage(st,alls)

            
        elif inputs==2:
            print(dic)
            f=input("If you want to search student name press 1 if not 2: ")
            if f==2:
                break
            elif 1:
                s=input("Enter the exact name: ")
                n=0
                for a,b in st.items():
                    if a==s:
                        print(a,'s score is',b)
                        break
                    elif len(st)==n:
                        print("student not found")
                    else:
                        n+=1
                        continue
                    

        elif inputs==3:
            print("Exit")
            break
    except:
        print("invalid selection")
        
    
