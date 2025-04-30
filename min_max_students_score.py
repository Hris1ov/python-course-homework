students_score = {
    "Ivan": 5.00,
    "Alex": 3.50,
    "Maria": 5.50,
    "George": 5.00
}

for student in students_score:
    if students_score[student] == max(students_score.values()):
        print(student, students_score[student])
    if students_score[student] == min(students_score.values()):
        print(student, students_score[student])                     