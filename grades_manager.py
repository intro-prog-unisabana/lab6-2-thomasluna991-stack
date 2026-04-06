def initialize_dict(student_name, subject_grades):
    return {student_name: subject_grades}


def add_student(student_grades=None):
    if student_grades is None:
        student_grades = {}

    name = input("Enter student name:\n").strip().title()
    subjects = {}

    while True:
        entry = input("Enter subject and grade (or 'exit' to finish):\n").strip()
        
        if entry.lower() == "exit":
            break
        
        subject, grade = entry.split(",")
        subject = subject.strip().title()
        grade = float(grade.strip())
        
        subjects[subject] = grade

    student_grades[name] = subjects
    print(f"Student {name} successfully added to the grades management system.\n")

    return student_grades


def get_students(student_grades, keys):
    result = {}

    for key in keys:
        found = False
        for student in student_grades:
            if student.lower() == key.lower():
                result[student.title()] = student_grades[student]
                found = True
                break
        
        if not found:
            print(f"{key.title()} not found!")

    return result


def avg_by_student(student_grades, keys=None):
    if keys is None:
        selected = student_grades
    else:
        selected = get_students(student_grades, keys)

    for student, grades in selected.items():
        avg = sum(grades.values()) / len(grades)
        print(f"{student}: {round(avg, 1)}")