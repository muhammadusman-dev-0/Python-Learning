# Topic: Conditional Statements (if, elif, else)
marks = 85

if marks < 0 or marks > 100:
    print("Invalid marks")
elif marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print("Grade C")
elif marks >= 50:
    print("Grade D")
else:
    print("Fail")
