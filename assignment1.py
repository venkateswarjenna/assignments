# Task 1: Take Fee Details as Input

student_id = int(input("Enter Student ID: "))
student_name = input("Enter Student Name: ")
course = input("Enter Course Name: ")
semester = int(input("Enter Semester: "))
total_fee = float(input("Enter Total Fee: "))
paid_fee = float(input("Enter Paid Fee: "))
remaining_fee = total_fee - paid_fee

# Create tuple for fee breakdown
fee_details = (total_fee, paid_fee, remaining_fee)

# Calculate fee paid percentage
paid_percentage = (paid_fee / total_fee) * 100

# Subjects enrolled (comma-separated)
subjects = input("Enter Subjects (comma-separated): ").split(',')

# Scholarships (use set to avoid duplicates)
scholarships = set(input("Enter Scholarships (comma-separated if any): ").split(','))

# Guardian info (dictionary)
guardian_name = input("Enter Guardian Name: ")
guardian_contact = input("Enter Guardian Contact Number: ")
guardian_address = input("Enter Guardian Address: ")
guardian_info = {
    "Name": guardian_name,
    "Contact": guardian_contact,
    "Address": guardian_address
}

# Task 2: Display Using Different Formatting Methods

# 1. Comma Separation
print("\n--- Using Comma Separation ---")
print("Student ID, Name, Course:", student_id, student_name, course, sep=', ')

# 2. Percentage Formatting
print("\n--- Using Percentage Formatting ---")
print("Fee Paid: %.2f%%" % paid_percentage)

# 3. f-strings
print("\n--- Using f-strings ---")
print(f"Student: {student_name} (ID: {student_id})")
print(f"Course: {course} | Semester: {semester}")
print(f"Total Fee: ₹{fee_details[0]:.2f}")
print(f"Paid: ₹{fee_details[1]:.2f} | Remaining: ₹{fee_details[2]:.2f}")
print(f"Subjects: {', '.join([s.strip() for s in subjects])}")
print(f"Scholarships: {', '.join([s.strip() for s in scholarships])}")

# 4. .format() Method
print("\n--- Using .format() Method ---")
print("Guardian Info: Name - {}, Contact - {}, Address - {}".format(
    guardian_info["Name"], guardian_info["Contact"], guardian_info["Address"]
))
