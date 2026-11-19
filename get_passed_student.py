def get_passed_student(marks: dict) -> list:
    """This function takes the average grade of each student defined in the
    previous function and the names, and if the grade is 5 or better the
    program puts the name of the student on a new list.
    The inputs will be the average grade and the name of each student.
    The output will be a list with the name of the students that have
    passed."""
    passed_list = []
    for student_name in marks:
      average = calculate_students_average(marks, student_name)
      if average >= 5:
        passed_list.append(student_name)
    return passed_list
