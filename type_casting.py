# Topic: Type Casting
print("======= MARKS AND PERCENTAGE CALCULATOR =======")

obtained_marks = "425"
total_marks = "500"

obtained_marks = int(obtained_marks)
total_marks = int(total_marks)

percentage = (obtained_marks / total_marks) * 100

print("Obtained Marks:", obtained_marks)
print("Total Marks:", total_marks)
print("Percentage:", round(percentage, 2), "%")
