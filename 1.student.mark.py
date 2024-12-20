students = {}
courses = {}
marks = {}
SEPARATOR = "----------"

# ================== UTILITIES ==================
def checkData():
    global courses, students
    if len(courses) == 0 or len(students) == 0:
        print("Please enter course and student information first.")
        return 0
    return 1

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

# ================== ACTIONS ==================
def entryAction():
    action = input()
    match action:
        case "c":
            enterCourseInfo()
        case "s":
            enterStudentInfo()
        case "m":
            if checkData():
                enterMarkInfo()
        case _:
            print("Unrecognized action. Please enter the correct key")

def displayAction():
    action = input()
    match action:
        case 'c':
            displayCourses()
        case 's':
            displayStudents()
        case 'm':
            displayMarks()
        case _:
            print("Unrecognized action. Please enter the correct key")

# ================== COURSES ==================
def enterNumberOfCourses():
    print("Enter the number of courses:")
    numberOfCourses = int(input(">>>"))
    return numberOfCourses

def enterCourseInfo():
    global courses
    amountOfCourses = enterNumberOfCourses()
    for i in range(amountOfCourses):
        print("Enter course's information: ")
        print("ID: ", end='')
        id = input()
        print("Name: ", end='')
        name = input()
        courses[id] = name
    return

# ================== STUDENTS ==================
def enterNumberOfStudents():
    print("Enter the number of students:")
    numberOfStudent = int(input(">>>"))
    return numberOfStudent

def enterStudentInfo():
    global students
    amountOfStudents = enterNumberOfStudents()
    for i in range(amountOfStudents):
        print("Enter student's information: ")
        print("ID: ", end='')
        id = input()
        print("Name: ", end='')
        name = input()
        print("Date of Birth: ", end='')
        dob = input()
        students[id] = { "name": name, "dob": dob }
    return

# ================== MARKS ==================
def enterMark():
    print("Enter the number of marks: ")
    numberOfMarks = int(input(">>>"))
    return numberOfMarks

def isValidCourseID(courseID):
    return courseID in courses

def isValidStudentID(studentID):
    return studentID in students

def enterMarkInfo():
    global marks
    amountOfMarks = enterMark()
    for i in range(amountOfMarks):
        print("Enter mark's information: ")
        print("Course ID: ", end='')

        while True:
            courseID = input()
            if isValidCourseID(courseID):
                break
            else:
                print("Invalid course ID. Please enter again.")

        print("Student ID: ", end='')
        while True:
            studentID = input()
            if isValidStudentID(studentID):
                break
            else:
                print("Invalid student ID. Please enter again.")

        print("Mark: ", end='')
        mark = float(input())
        marks[courseID] = { "studentID": studentID, "mark": mark }
    return

# ================== DISPLAY ==================
def displayCourses():
    global courses
    for course in courses:
        print(f"ID: {course}, Name: {courses[course]}")
    return

def displayStudents():
    global students
    for student in students:
        print(f"ID: {student}, Name: {students[student]['name']}, DoB: {students[student]['dob']}")
    return

def displayMarks():
    global marks
    for mark in marks:
        print(f"Course ID: {mark}, Student ID: {marks[mark]['studentID']}, Mark: {marks[mark]['mark']}")

def main():
    while True:
        welcomeMessage()
        action = input()
        match action:
            case 'q':
                exit()
            case 'e':
                entryMessage()
                entryAction()
            case 'd':
                displayMessage()
                displayAction()
            case _:
                print("Unrecognized action. Please enter the correct key")

if __name__ == "__main__":
    main()
