class Student:
    """
    Represents a student with attributes like name, age, roll number, etc.
    """
    def __init__(self, name, age, rollno, branch, userId, phone, hobby, add):
        """
        Initializes a student object with input validation.
        """
        if not isinstance(age, str):  
            raise ValueError("Age must be a string.")
        if not age.isdigit() or int(age) <= 0:
            raise ValueError("Age must be a positive integer.")
        if not phone.isdigit() or len(phone) != 10:
            raise ValueError("Phone must be a 10-digit number.")

        self.name = name
        self.age = int(age)
        self.rollno = rollno
        self.branch = branch
        self.userID = userId
        self.phone = phone
        self.hobby = hobby
        self.add = add

    def display_student(self):
        """
        Prints all attributes of the student.
        """
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll No : {self.rollno}")
        print(f"Branch Name : {self.branch}")
        print(f"UserId : {self.userID}")
        print(f"Phone No. : {self.phone}")
        print(f"Hobby : {self.hobby}")
        print(f"Address : {self.add}")
