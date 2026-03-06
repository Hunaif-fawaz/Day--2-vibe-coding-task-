# Advanced Grade Calculator Program

while True:
    # Ask for student's name
    name = input("\nEnter the student's name (type 'Exit' to stop): ")

    # Exit condition
    if name.lower() == "exit":
        print("Program ended.")
        break

    # Input marks
    mark1 = float(input("Enter marks for Subject 1: "))
    mark2 = float(input("Enter marks for Subject 2: "))
    mark3 = float(input("Enter marks for Subject 3: "))

    # Calculate average
    average = (mark1 + mark2 + mark3) / 3

    # Determine grade
    if average >= 75:
        grade = "A"
    elif average >= 60:
        grade = "B"
    elif average >= 40:
        grade = "C"
    else:
        grade = "Fail"

    # Print clean formatted output
    print("------------------------------")
    print("Name    :", name)
    print("Average :", round(average, 2))
    print("Grade   :", grade)
    print("------------------------------")