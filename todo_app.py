todo_list = []

def add_task():
    task = input("Enter a new task: ")
    todo_list.append(task)
    print(f"Task '{task}' added successfully!")

def delete_task():
    if len(todo_list) <= 0 :
        print("there is no task!")
    else:
        task_num = int(input("Enter task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
        print(f"Task '{removed_task}' deleted successfully!")
            
            
def display():
    if not todo_list:
        print("The list is Empty!!")
    else:
        for item in todo_list:
            print(item)
            
            
while True:
    print("\n1. Add Task | 2. View Tasks | 3. Delete Task | 4. Exit")
    choice = input("Enter choice (1-4): ")
    
    if choice == '1' :
        add_task()
    elif choice == '2' :
        display()
    elif choice == '3' :
        delete_task()
    elif choice == '4' : 
        print("Goodbye!!")  
        break
    else:
        print("Invalid input..")        
        
                  
            
    

        

                    
                
        
