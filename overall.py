def student_averages(students):
    result = {}
    for student, grades in students.items():
        avg = sum(grades.values()) / len(grades)
        result[student] = round(avg)
    return result


def assignment_averages(students):
    result = {}
    for assignment in next(iter(students.values())).keys():
        total = 0
        count = 0
        for grades in students.values():
            total += grades[assignment]
            count += 1
        result[assignment] = round(total / count)
    
    return result