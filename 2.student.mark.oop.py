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

class SchoolManagement:
    def __init__(self):
        self.courses = CourseCollection()
        self.students = StudentCollection()
        self.marks = MarkCollection()

    def entry_action(self):
        action = input()
        match action:
            case "c":
                self.courses.enter()
            case "s":
                self.students.enter()
            case "m":
                self.marks.enter()
            case _:
                print("Unrecognized action. Please enter the correct key")

    def display_action(self, action):
        match action:
            case 'c':
                self.courses.display()
            case 's':
                self.students.display()
            case 'm':
                self.marks.display()
            case _:
                print("Unrecognized action. Please enter the correct key")

# ================== MESSAGES ==================
def welcomeMessage():
    print(SEPARATOR)
    print("q - quit")
    print("e - enter data")
    print("d - display data")
    print(">>>", end='')

def entryMessage():
    print(SEPARATOR)
    print("Choose the data you want to enter:")
    print("c - course information")
    print("s - student information")
    print("m - mark")
    print(">>>", end='')

def displayMessage():
    print(SEPARATOR)
    print("Choose the data you want to display:")
    print("c - courses")
    print("s - students")
    print("m - mark")
    print(">>>", end='')

# ================== MAIN ==================
def main():
    school = SchoolManagement()
    while True:
        welcomeMessage()
        action = input()
        match action:
            case 'q':
                exit()
            case 'e':
                entryMessage()
                school.entry_action()
            case 'd':
                displayMessage()
                school.display_action(input())
            case _:
                print("Unrecognized action. Please enter the correct key")

if __name__ == "__main__":
    main()
