def calculate_student_average(marks: tuple, student: str) -> float:
    """This function calculates the average mark of a specific student inside a
    dictionary of tuples composed by the student’s name and a list of their marks.
    The input must be the dictionary of tuples and the name of the student.
    The output will be his average mark."""
    for subtuple in marks:
        if subtuple[0] == student:
            return float(sum(subtuple[1]) / len(subtuple[1]))
    return f"{student} is not part of the class"
