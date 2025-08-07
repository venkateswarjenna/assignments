

student_id = int(input("Enter Student ID: "))
student_name = input("Enter Student Name: ")
course = input("Enter Course Name: ")
semester = int(input("Enter Semester: "))
total_fee = float(input("Enter Total Fee: "))
paid_fee = float(input("Enter Paid Fee: "))
remaining_fee = total_fee - paid_fee


fee_details = (total_fee, paid_fee, remaining_fee)


paid_percentage = (paid_fee / total_fee) * 100


subjects = input("Enter Subjects (comma-separated): ").split(',')


scholarships = set(input("Enter Scholarships (comma-separated if any): ").split(','))


guardian_name = input("Enter Guardian Name: ")
guardian_contact = input("Enter Guardian Contact Number: ")
guardian_address = input("Enter Guardian Address: ")
guardian_info = {
    "Name": guardian_name,
    "Contact": guardian_contact,
    "Address": guardian_address
}




print("\n--- Using Comma Separation ---")
print("Student ID, Name, Course:", student_id, student_name, course, sep=', ')


print("\n--- Using Percentage Formatting ---")
print("Fee Paid: %.2f%%" % paid_percentage)


print("\n--- Using f-strings ---")
print(f"Student: {student_name} (ID: {student_id})")
print(f"Course: {course} | Semester: {semester}")
print(f"Total Fee: ₹{fee_details[0]:.2f}")
print(f"Paid: ₹{fee_details[1]:.2f} | Remaining: ₹{fee_details[2]:.2f}")
print(f"Subjects: {', '.join([s.strip() for s in subjects])}")
print(f"Scholarships: {', '.join([s.strip() for s in scholarships])}")


print("\n--- Using .format() Method ---")
print("Guardian Info: Name - {}, Contact - {}, Address - {}".format(
    guardian_info["Name"], guardian_info["Contact"], guardian_info["Address"]
))
