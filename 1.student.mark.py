def welcomeMessage():
    print("q - quit")
    print("e - enter data")
    print("d - display data")

def entryMessage():
    return 

def displayMessage():
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
            case 'd': 
                displayMessage()
            case _: 
                print("Unrecognized action")

if __name__ == "__main__":
    main()
