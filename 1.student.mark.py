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

def enterNumberOfStudents():
    return 

def enterStudentInfo():
    return 

def enterNumberOfCourses():
    return

def enterCourseInfo():
    return 

def enterMark():
    return

def displayCourses():
    return 

def displayStudents():
    return 

def displayMarks():
    return 

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
