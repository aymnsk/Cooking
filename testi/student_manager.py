import json
from student import Student

class StudentManager:
    """
    Manages the list of students and provides methods to add, display, update, delete, save, and load students.
    """
    def __init__(self):
        """
        Initializes an empty list of students and loads existing data if available.
        """
        self.students = []
        self.load_students()

    def add_student(self, student):
        """
        Adds a student to the list if they are valid and not a duplicate.
        """
        # Check for duplicate rollno
        if any(s.rollno == student.rollno for s in self.students):
            print(f"Student with roll number {student.rollno} already exists.")
            return
        
        # Add the student if they pass validation
        self.students.append(student)
        print("Student added successfully.")
        self.save_students()

    def display_all_students(self):
        """
        Displays all students in the list.
        """
        if not self.students:
            print("No students found.")
            return
        for student in self.students:
            student.display_student()

    def get_student_by_rollno(self, rollno):
        """
        Returns the student with the specified roll number.
        """
        for student in self.students:
            if student.rollno == rollno:
                return student
        print("Student not found.")
        return None

    def update_student(self, rollno, **kwargs):
        """
        Updates the details of a student with the specified roll number.
        """
        student = self.get_student_by_rollno(rollno)
        if student:
            for key, value in kwargs.items():
                if hasattr(student, key):
                    setattr(student, key, value)
                    print(f"{key} updated successfully.")
                else:
                    print(f"Invalid attribute: {key}")
            self.save_students()

    def delete_student(self, rollno):
        """
        Deletes a student from the list by their roll number.
        """
        initial_count = len(self.students)
        self.students = [s for s in self.students if s.rollno != rollno]
        if len(self.students) < initial_count:
            print("Student deleted successfully.")
        else:
            print("Student not found.")
        self.save_students()

    def save_students(self, filename="students.json"):
        """
        Saves the list of students to a JSON file.
        """
        with open(filename, "w") as file:
            json.dump([s.__dict__ for s in self.students], file)
        print("Data saved successfully.")

    def load_students(self, filename="students.json"):
        """ Loads the list of students from a JSON file 
            and handles any key name mismatches."""
        try:
            with open(filename, "r") as file:
                data = json.load(file)
                # Mapping key 'userID' to 'userId' and any other mismatches
                for student_data in data:
                    if 'userID' in student_data:
                        student_data['userId'] = student_data.pop('userID')
                    # Convert age to string if it's not already a string
                    if isinstance(student_data['age'], int):
                        student_data['age'] = str(student_data['age'])
                # Convert to Student objects
                self.students = [Student(**s) for s in data]
                print("Data loaded successfully.")
        except FileNotFoundError:
            print("No saved data found.")
