from student import Student
from student_manager import StudentManager

def main():
    manager = StudentManager()

    while True:
        print("Student Management System")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Exit")

        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            name = input("Enter student Name: ")
            age = input("Enter student age: ")
            rollno = input("Enter student roll no: ")
            branch = input("Enter student branch: ")
            userId = input("Enter student UserId: ")
            phone = input("Enter student Phone no: ")
            hobby = input("Enter student hobby: ")
            add = input("Enter student address: ")

            student = Student(name,age,rollno,branch,userId,phone,hobby,add)
            manager.add_student(student)
            print("Student added successfully!")

        elif choice == 2:
            manager.display_all_students()
        elif choice == 3:
            print("exiting the system...")
            break
        else:
            print("Invalid Choice")
# if __name__ == "__main__":
main()