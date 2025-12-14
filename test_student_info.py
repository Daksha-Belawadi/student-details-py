from student_info import student_info

def test_student_info():
    result = student_info("Daksha", 186, "BCA", 98)
    expected = "Student Name: Daksha, Roll No: 186, Course: BCA, Marks: 98"
    assert result == expected
