SEPARATOR = "----------"

def welcomeMessage():
    print(SEPARATOR)
    print("q - quit")
    print("e - enter data")
    print("d - display data")

def entryMessage():
    print(SEPARATOR)
    print("Choose the data you want to enter:")
    print("ns - number of students")
    print("si - student information")
    print("nc - number of courses")
    print("ci - course information")
    print("mk - mark")

def displayMessage():
    print(SEPARATOR)
    print("Choose the data you want to display:")
    print("c - courses")
    print("s - students")
    print("m - mark")

def entryAction():
    return

def displayAction():
    return

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
                print("Unrecognized action")

if __name__ == "__main__":
    main()
