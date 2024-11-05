# Step 1: Collecting student data
name = input("Enter the student's name: ")  # Collects the student's name
birth_date = input("Enter the birth date (format: DD/MM/YYYY): ")  # Collects the birth date
class_number = input("Enter the class number: ")  # Collects the class number

# Step 2: Collecting grades in three subjects
math_grade = float(input("Enter the grade in Math: "))  # Collects the grade in Math
english_grade = float(input("Enter the grade in English: "))  # Collects the grade in English
physics_grade = float(input("Enter the grade in Physics: "))  # Collects the grade in Physics

# Step 3: Calculating the average grade
average_grade = (math_grade + english_grade + physics_grade) / 3  # Calculates the average

# Step 4: Displaying the information and the grades
print(f"\nStudent's name: {name}")
print(f"Birth date: {birth_date}")
print(f"Class number: {class_number}")
print(f"Average grade: {average_grade:.2f}")  # Shows the average with two decimal places
