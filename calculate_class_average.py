
def calculate_class_average(data: dict[str, list[float]]) -> float:
    """
    Compute the average grade of all students in the class.

    Args:
        data (dict[str, list[float]]): Student name -> list of test marks.

    Returns:
        float: The average score of all students, or 0.0 if there are no students.

    Example:
        calculate_class_average({"Ana": [8, 7, 9], "Luis": [4, 5, 3]}) -> 6.0
    """
    # Return 0.0 if there are no students
    if not data:
        return 0.0

    # Calculate the average score of each student
    average_score_marks = [calculate_student_average(marks) for marks in data.values()]

    # Return the average score of all students
    return sum(average_score_marks) / len(average_score_marks)
