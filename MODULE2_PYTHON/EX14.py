def assign_grade(score: int) -> None:
    if score >= 90:
        grade = "A"
    elif score >= 75:
        grade = "B"
    else:
        grade = "C"
    print(f"Score: {score}, Grade: {grade}")

assign_grade(88)
