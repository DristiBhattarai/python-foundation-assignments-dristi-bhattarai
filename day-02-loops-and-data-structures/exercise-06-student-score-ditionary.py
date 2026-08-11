"""
Exercise: Student Score Dictionary
Student: Dristi Bhattarai
Day: 2
"""
student_scores = {
    "Anisha": 78,
    "Ravi": 55,
    "Maya": 92,
    "Sagar": 61,
    "Nima": 48
}

# 1. Print every student and score.
for student, score in student_scores.items():
    print(student, ":", score)

# 2. Students who scored at least 60.
passing_students = {
    student: score
    for student, score in student_scores.items()
    if score >= 60
}

# 3. Student with the highest score.
highest_student = max(student_scores, key=student_scores.get)
highest_score = student_scores[highest_student]

# 4. Average score.
average_score = sum(student_scores.values()) / len(student_scores)

print("\nPassing students:", passing_students)
print("Highest scorer:", highest_student, "-", highest_score)
print("Average score:", average_score)