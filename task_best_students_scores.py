students_score = {
    "Ivan": 5.00,
    "Alex": 3.50,
    "Maria": 5.50,
    "George": 5.00
}

best_students_scores = []

for student,score in students_score.items():
    if  score >= 4.00:
        best_students_scores.append(student)
        
print(best_students_scores)    