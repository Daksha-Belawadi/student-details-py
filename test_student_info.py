from student_info import student_info

def test_student_info():
    result = student_info("Daksha", 186, "BCA", 98)
    expected = "Student Name: Ananya, Roll No: 101, Course: BCA, Marks: 88"

    print(result)   

    assert result == expected
