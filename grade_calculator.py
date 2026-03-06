# Grade Calculator Program with Grades

# Ask for student's name
name = input("Enter the student's name: ")

# Ask for 3 subject marks
mark1 = float(input("Enter marks for Subject 1: "))
mark2 = float(input("Enter marks for Subject 2: "))
mark3 = float(input("Enter marks for Subject 3: "))

# Calculate the average
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

# Display results
print("\nStudent Name:", name)
print("Average Marks:", round(average, 2))
print("Grade:", grade)

# Display Pass/Fail
if average >= 40:
    print("Result: Pass")
else:
    print("Result: Fail")