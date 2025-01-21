from student import Student
from student_manager import StudentManager

def main():
    # Initialize the student manager which will load existing data
    manager = StudentManager()

    while True:
        # Display the menu
        print("Student Management System")
        print("1. Add Student")
        print("2. Display All Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")

        try:
            choice = int(input("Enter Your Choice: "))
        except ValueError:
            print("Invalid choice, please enter a valid number.")
            continue

        if choice == 1:
            # Add Student
            name = input("Enter student Name: ")
            age = input("Enter student age: ")
            rollno = input("Enter student roll no: ")
            branch = input("Enter student branch: ")
            userId = input("Enter student UserId: ")
            phone = input("Enter student Phone no: ")
            hobby = input("Enter student hobby: ")
            add = input("Enter student address: ")

            try:
                student = Student(name, age, rollno, branch, userId, phone, hobby, add)
                manager.add_student(student)
            except ValueError as e:
                print(f"Error adding student: {e}")

        elif choice == 2:
            # Display All Students
            manager.display_all_students()

        elif choice == 3:
            # Update Student
            rollno = input("Enter the roll number of the student to update: ")
            student = manager.get_student_by_rollno(rollno)
            if student:
                print("Enter the details you want to update (leave blank to skip):")
                name = input(f"Name ({student.name}): ") or student.name
                age = input(f"Age ({student.age}): ") or str(student.age)
                if age:
                    try:
                        age = int(age)
                    except ValueError:
                        print("Invalid age input. It should be an integer.")
                        continue
                branch = input(f"Branch ({student.branch}): ") or student.branch
                userId = input(f"UserId ({student.userID}): ") or student.userID
                phone = input(f"Phone ({student.phone}): ") or student.phone
                hobby = input(f"Hobby ({student.hobby}): ") or student.hobby
                address = input(f"Address ({student.add}): ") or student.add

                manager.update_student(rollno, name=name, age=age, branch=branch, userId=userId,
                                       phone=phone, hobby=hobby, add=address)

        elif choice == 4:
            # Delete Student
            rollno = input("Enter the roll number of the student to delete: ")
            manager.delete_student(rollno)

        elif choice == 5:
            # Exit the system
            print("Goodbye! Exiting the system...")
            break

        else:
            print("Invalid Choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
