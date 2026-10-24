students = [
    {"name": "Sara", "score": 85},
    {"name": "Ahmed", "score": 42},
    {"name": "Musa", "score": 93},
    {"name": "Hana", "score": 67},
]


def validate_score(score):
    if score < 0 or score > 100:
        raise ValueError("Score must be between 0 and 100.")


def calculate_grade(score):
    validate_score(score)

    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"


def calculate_average(students):
    if len(students) == 0:
        return None

    total = 0
    for student in students:
        total += student["score"]

    return total / len(students)


def find_highest_and_lowest(students):
    if len(students) == 0:
        return None

    highest = students[0]
    lowest = students[0]

    for student in students[1:]:
        if student["score"] > highest["score"]:
            highest = student
            if student["score"] < lowest["score"]:
                lowest = student

    return {"highest": highest, "lowest": lowest}


def count_passed_and_failed(students):
    passed = 0
    failed = 0

    for student in students:
        if student["score"] >= 50:
            passed += 1
        else:
            failed += 1

    return {"passed": passed, "failed": failed}


def students_above_average(students, average):
    above_average = []

    for student in students:
        if student["score"] > average:
            above_average.append(student)

    return above_average


def generate_class_report(students):
    if len(students) == 0:
        print("No student results to report.")
        return None

    for student in students:
        validate_score(student["score"])

        average = calculate_average(students)
        score_summary = find_highest_and_lowest(students)
        counts = count_passed_and_failed(students)
        above_average = students_above_average(students, average)

        print("CLASS REPORT")

        for student in students:
            grade = calculate_grade(student["score"])
            print(f'{student["name"]}: score = {student["score"]}, grade = {grade}')

            print(f"Class average: {average:.2f}")
            print(
                f'Highest score: {score_summary["highest"]["name"]} '
                f'({score_summary["highest"]["score"]})'
            )
            print(
                f'Lowest score: {score_summary["lowest"]["name"]} '
                f'({score_summary["lowest"]["score"]})'
            )
            print(f'Passed: {counts["passed"]}')
            print(f'Failed: {counts["failed"]}')

            print("Students above the class average:")
            for student in above_average:
                print(f'{student["name"]}: {student["score"]}')


generate_class_report(students)
