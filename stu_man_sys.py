class Student :
    def __init__(self, name, age , student_id , dept , cgpa):
        self.name = name 
        self.age = age 
        self.student_id = student_id
        self.dept = dept
        self.cgpa = cgpa



class StudentManager :
    def __init__(self):
        self.students = []
    def add_stu(self, student):
        self.students.append(student)

    def rmv_stu(self, stu_id):
        for student in self.students:
            if student.student_id == stu_id:
                self.students.remove(student)
                print("Student removed successfully.")
                return

        print("Student not found.")

    def show_stu(self):
        for student in self.students:
            print(student)

    def search_stu(self, stu_id):
        for student in self.students:
            if student.student_id == stu_id:
                print(student)

    def total_stu(self):
        count = 0
        for student in self.students:
            count = count + 1
        return count    


def menu():
    manager = StudentManager()

    while True:
        print("1. Add Student")
        print("2. Remove Student")
        print("3. Show All Students")
        print("4. Search Student")
        print("5. Total Students")
        print("6. Update Student")
        print("7. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            student_id = int(input("Enter student ID: "))
            dept = input("Enter department: ")
            cgpa = float(input("Enter CGPA: "))

            student = Student(name, age, student_id, dept, cgpa)

            manager.add_stu(student)

            print("Student added successfully.")

        elif choice == 2:
            stu_id = int(input("Enter student ID: "))
            manager.rmv_stu(stu_id)


        elif choice == 3:
            manager.show_stu()


        elif choice == 4:
            stu_id = int(input("Enter student ID: "))
            manager.search_stu(stu_id)


        elif choice == 5:
            print("Total students:", manager.total_stu())


        elif choice == 6:
            stu_id = int(input("Enter student ID: "))
            manager.update_stu(stu_id)


        elif choice == 7:
            print("Program exited.")
            break

        else:
            print("Invalid choice.")


menu()