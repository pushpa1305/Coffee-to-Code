def average_passing_grades(grades: list[int]) -> float:
    passing_grades = [g for g in grades if g >= 50]
    if not passing_grades:
        return 0.0
    total_sum = sum(passing_grades)
    count = len(passing_grades)
    return float(total_sum / count)
