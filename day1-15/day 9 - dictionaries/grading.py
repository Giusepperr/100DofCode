student_scores = {
    "ST1": 80,
    "ST2": 27,
    "ST3": 80,
    "ST4": 99,
    "ST5": 78,
    "ST6": 76,
}

student_grades = {}
for student in student_scores:
    grade = 'you are a pussy'
    if student_scores[student] > 90:
        grade = 'A-mazzing'
    elif student_scores[student] >=80:
        grade = 'Fuck This'
    elif student_scores[student] >60:
        grade = 'Funky but bland'   
    student_grades[student]= grade
print(student_grades)
