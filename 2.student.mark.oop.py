SEPARATOR = "----------"

# ================== CLASSES ==================
class Student:
    def __init__(self, id, name, dob):
        self.id = id
        self.name = name
        self.dob = dob

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, DoB: {self.dob}"

class Course:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}"

class Mark:
    def __init__(self, courseID, studentID, mark):
        self.courseID = courseID
        self.studentID = studentID
        self.mark = mark

    def __str__(self):
        return f"Course ID: {self.courseID}, Student ID: {self.studentID}, Mark: {self.mark}"

class Collection:
    def getAmount(self):
        amount = int(input("Enter amount: "))
        return amount

    def enter(self):
        pass

    def display(self):
        for item in self.items:
            print(item)

class CourseCollection(Collection):
    def __init__(self):
        self.items = {}

    def enter(self):
        amount = self.getAmount()
        for _ in range(amount):
            id = input("Enter course ID: ")
            name = input("Enter course name: ")
            self.items[id] = Course(id, name)

    def display(self):
        print(SEPARATOR)
        for course in self.items.values():
            print(course)

class StudentCollection(Collection):
    def __init__(self):
        self.items = {}

    def enter(self):
        amount = self.getAmount()
        for _ in range(amount):
            id = input("Enter student ID: ")
            name = input("Enter student name: ")
            dob = input("Enter student DoB: ")
            self.items[id] = Student(id, name, dob)

    def display(self):
        print(SEPARATOR)
        for student in self.items.values():
            print(student)

class MarkCollection(Collection):
    def __init__(self):
        self.items = {}

    def enter(self):
        amount = self.getAmount()
        for _ in range(amount):
            courseID = input("Enter course ID: ")
            studentID = input("Enter student ID: ")
            mark = input("Enter mark: ")
            self.items[(courseID, studentID)] = Mark(courseID, studentID, mark)

    def display(self):
        print(SEPARATOR)
        for mark in self.items.values():
            print(mark)
# ================== MESSAGES ==================
# ================== MAIN ==================
def main():
if __name__ == "__main__":
    main()
