# Topic: Tuples
student_record = ("Usman", 16, 85, 92, 78)

print("======= STUDENT RECORD =======")
print("Name:", student_record[0])
print("Age:", student_record[1])
print("Marks:", student_record[2:])
print("Number of subjects:", len(student_record) - 2)
print("Highest mark:", max(student_record[2:]))
