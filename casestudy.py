#Author: Amade Monisola
# File Name: student_gpa_checker.py
# Description: This app accepts student names and GPAs, and checks if each student qualifies for the Dean's List (GPA ≥ 3.5) or Honor Roll (GPA ≥ 3.25). The programstops when the user enters 'ZZZ' as the last name
while True:
    lname = input("What is your last name (or enter 'ZZZ' to end program): ")
    if lname == "ZZZ":
        print("End of program")
        break
    fname = input("What is your first name: ")
    print("Hello,"+" "+fname + " " + lname)
    gpa = float(input("What is your Gpa: "))
    if gpa >= 3.5:
        print("Congratulations "+fname +" " + lname + " you are a high achiever and are on the dean's list.")
    elif gpa >= 3.25:
        print("Congratulations "+fname +" " + lname + " you have made the honor roll")
    elif gpa > 4.0 or gpa < 0.0:
        print("Enter a valid gpa.")    
    else:
        print("Your gpa has been recorded.")
