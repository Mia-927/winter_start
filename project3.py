#ToDo管理ミニアプリ

"""ToDoを追加できる

ToDo一覧を表示できる

完了したToDoをマークできる"""

def addTodo(todos,title):
    do={"title":title,'done':False}
    todos.append(do)
    #ｌｓｔ系は自分で変えてくれるreturn todos

def checkTodo(todos,title):
    path=False
    for todo in todos:
        if todo["title"]==title:
            todo['done'] =True
            path=True
            print("checkout success")
            break
    if path==False:
        print("not found")
    return todos

todos=[]
do={}
#Menu
while 1:
    print('Main menu','1.Add ToDo','2.Show ToDo','3,checkout ToDo','4.Exit',sep='\n')
    select=int(input("Enter selection: "))
    if select==1:
        do=input("What do you want to add in the ToDo list? :")
        addTodo(todos,do)
        print("This is added",do,"This is on the ToDo list",todos)
    elif select==2:
        print(todos)
    elif select==3:
        done=input("What do you want to checkout in the ToDo list? :")
        checkTodo(todos,done)
        print(todos,"left and",done,"are done!")
    elif select==4:
        break
    
