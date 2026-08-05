contact_book = {}
def add_contact():
    name = input("enter contact name : ")
    phoneNUM = int(input("Enter phone number : "))
    contact_book [name] = phoneNUM
    print(f"{name} and {phoneNUM} is added!")
    
def view_contact():
        for item , number in contact_book.items():
            print(item , number)
            
            
def delete_contact():
    if not contact_book:
        print("the contact book is empty..")
    else:
        name = input("Enter your name : ")
        del contact_book[name]


while True:
    print("\n1. Add contact| 2. View contact | 3. Delete contact | 4. Exit")
    choice = input("Enter your (1 - 4) number choice : ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contact()
    elif choice == '3':
        delete_contact()
    elif choice == '4':
        print("Goodbye!")
        break
    else:
        print("Invalid input....")


                                
                      