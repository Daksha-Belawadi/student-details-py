from student import student_details

def test_student_details():
    expected_output = (
        "Student ID: S101\n"
        "Student Name: Ananya\n"
        "Course: BCA\n"
        "Marks: 88"
    )

    assert student_details("S101", "Ananya", "BCA", 88) == expected_output
