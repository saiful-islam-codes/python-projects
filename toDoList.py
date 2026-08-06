toDoList = []

def add_list():
    work = input("Enter your task : ")
    toDoList.append(work)
    print("Added..")

def delt_list():
    work = input("Enter your task : ")
    if work in toDoList: 
        toDoList.remove(work)
    else:
        print("Can not find it..")

def mark_done():
    work = input("Enter your task : ")  
    if work in toDoList:
        pos = toDoList.index(work)
        toDoList[pos] = print(f"{work} [Done]")      
    else:
        print("Can not find..")
            
while True:
    print("\n1. Add Task  2. Delete Task  3. Mark Done  4. Exit")
    choice = input("Enter choice (1-5): ")
    
    if choice == "1":
        add_list()
    elif choice == "2":
        delt_list()
    elif choice == "3":
        mark_done()        
    elif choice == "4":
        print("Goodbye!")
        break
    else:
        print("Invalid Choice!")