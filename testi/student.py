class Student:
    def __init__(self,name,age,rollno,branch,userId,phone,hobby,add):
        self.name = name
        self.age = age
        self.rollno = rollno
        self.branch = branch
        self.userID = userId
        self.phone = phone
        self.hobby = hobby
        self.add = add
       
    def display_student(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Roll No : {self.rollno}")
        print(f"Branch Name :{self.branch}")
        print(f"UserId :{self.userID}")
        print(f"Phone No. :{self.phone}")
        print(f"Hobby :{self.hobby}")
        print(f"Address :{self.add}")
