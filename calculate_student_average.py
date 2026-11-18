def calculate_student_average(marks: dict, student: str) -> float | str:
    """This function calculates the average mark of a specific student inside a
    dictionary composed by the student’s name and a list of their
    marks.
    The input must be a dictionary with the student’s name as key and their value a list of his marks..
    The output will be his average mark."""
    if student in marks:
        return float(sum(marks[student]) / len(marks[student]))
    return f"{student} is not part of the class"
    
