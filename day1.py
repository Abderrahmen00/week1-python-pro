from typing import TypedDict

class Grades(TypedDict):
    name: str
    ass_avg: float
    exam_avg: float
    final_grade: float
    letter_grade: str



def get_letter_grade(grade: float) -> str:
    if grade >= 90:
        return "A"
    elif grade >= 80:
        return "B"
    elif grade >= 70:
        return "C"
    elif grade >= 60:
        return "D"
    else:
        return "F"

def calculate_final_grade(name: str, assignment_scores: list[float], exam_scores: dict[str, float], bonus: float = 0) -> Grades:
    assAvg: float = sum(assignment_scores) / len(assignment_scores)
    examAvg: float = sum(exam_scores.values()) / len(exam_scores)
    finalGrade: float = 0.4*assAvg + 0.6*examAvg + bonus
    letterGrade: str = get_letter_grade(finalGrade)
    
    return {"name": name, "ass_avg": assAvg, "exam_avg": examAvg, "final_grade": finalGrade, "letter_grade": letterGrade}

# Test 1 — strong student
student1 = calculate_final_grade(
    name="Ali",
    assignment_scores=[85.0, 90.0, 78.0, 92.0],
    exam_scores={"midterm": 88.0, "final": 94.0},
    bonus=2.0
)
print(student1)

# Test 2 — average student
student2 = calculate_final_grade(
    name="Sana",
    assignment_scores=[60.0, 70.0, 65.0],
    exam_scores={"midterm": 72.0, "final": 68.0},
)
print(student2)

# Test 3 — failing student
student3 = calculate_final_grade(
    name="Malek",
    assignment_scores=[40.0, 50.0, 35.0],
    exam_scores={"midterm": 45.0, "final": 50.0},
)
print(student3)


    
    
    
     

    



