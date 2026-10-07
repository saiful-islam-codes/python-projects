class Book:
    def __init__(self, title, author, book_id):
        self.title = title
        self.author = author
        self.book_id = book_id 
        self.available = True




class Member:
    def __init__(self, name, member_id):
        self.info = []
        self.name = name
        self.member_id = member_id

    def borrow_book(self, book_id):
        self.info.append(book_id)



class Library:
    def __init__(self):
        self.book_list = []
        self.member_list = []

    def add_book(self, book):
        self.book_list.append(book)

    def rmv_book(self, book):
        self.book_list.remove(book) 

    def show_book(self):
        for i in self.book_list:
            print(i)       

    def total_book(self):
        count = 0 
        for i in self.book_list:
            count = count + 1
        return count        

    def search_book(self, book_id):
        for i in self.book_list:
            if i.book_id == book_id:
                return i

        print("book not found.")      
    def search_book(self, book_id):
        for book in self.book_list:
            if book.book_id == book_id:
                print("Title:", book.title)
                print("Author:", book.author)
                print("Book ID:", book.book_id)
                print("Available:", book.available)
                return book

        print("Book not found.")

    def add_member(self, member):
        self.member_list.append(member)

    def borrow_book(self, member_id, book_id):
        for member in self.member_list:
            if member.member_id == member_id:
                 for book in self.book_list:
                     if book.book_id == book_id and book.available:
                         member.borrow_book(book_id)
                         book.available = False
                         print("Book borrowed.")


    def return_book(self, member_id, book_id):
        for member in self.member_list:
            if member.member_id == member_id:
                if book_id in member.info:
                    member.info.remove(book_id)

                    for book in self.book_list:
                        if book.book_id == book_id:
                            book.available = True

                        print("Book returned.")                         

    def show_members(self):
        for i in self.member_list:
            print (i)





def menu():
    
    library = Library()

    while True:

        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Remove Book")
        print("3. Show Books")
        print("4. Search Book")
        print("5. Total Books")
        print("6. Add Member")
        print("7. Borrow Book")
        print("8. Return Book")
        print("9. Show Members")
        print("10. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:

            title = input("Enter book title: ")
            author = input("Enter author: ")
            book_id = int(input("Enter book ID: "))

            book = Book(title, author, book_id)

            library.add_book(book)

        elif choice == 2:

            book_id = int(input("Enter book ID: "))

            library.rmv_book(book_id)

        elif choice == 3:

            library.show_book()

        elif choice == 4:

            book_id = int(input("Enter book ID: "))

            library.search_book(book_id)

        elif choice == 5:

            print("Total books:", library.total_book())

        elif choice == 6:

            name = input("Enter member name: ")
            member_id = int(input("Enter member ID: "))

            member = Member(name, member_id)

            library.add_member(member)

        elif choice == 7:

            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))

            library.borrow_book(member_id, book_id)

        elif choice == 8:

            member_id = int(input("Enter member ID: "))
            book_id = int(input("Enter book ID: "))

            library.return_book(member_id, book_id)

        elif choice == 9:

            library.show_members()

        elif choice == 10:

            print("Program exited.")
            break

        else:

            print("Invalid choice.")


menu()

