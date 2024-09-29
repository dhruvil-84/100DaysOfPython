student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}

student_grades = {}
def grades(key, marks):
    if marks > 90 and marks <= 100:
        student_grades[key] = "Outstanding"
    elif marks > 80 and marks <= 90:
        student_grades[key] = "Exceeds Expectations"
    elif marks > 70 and marks <= 80:
        student_grades[key] = "Acceptable"
    else:
        student_grades[key] = "Fail"

for key in student_scores:
    grades(key, student_scores[key])
print(student_grades)
print(student_scores)