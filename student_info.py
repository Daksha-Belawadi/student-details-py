def student_details(student_id, name, course, marks):
    result = (
        f"Student ID: {student_id}\n"
        f"Student Name: {name}\n"
        f"Course: {course}\n"
        f"Marks: {marks}"
    )
    return result


if __name__ == "__main__":
    # Sample input
    student_id = "S101"
    name = "Ananya"
    course = "BCA"
    marks = 88

    print(student_details(student_id, name, course, marks))
