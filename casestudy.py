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
    elif gpa > 5.0 or gpa < 0.0:
        print("Enter a valid gpa.")    
    else:
        print("Your gpa has been recorded.")
