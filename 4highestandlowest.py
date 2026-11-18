from calculate_student_average import calculate_student_average


def find_highest_and_lowest(
    data: dict[str, list[float]]
) -> tuple[str, float, str, float]:
    """
    Find the highest and lowest student averages.

    Args:
        data: A non-empty dictionary of student names and their test marks.
              Each student has at least one mark (between 0 and 10).

    Returns:
        The names and average grades of the students
        with the highest and lowest averages.

    Example:
        >>> find_highest_and_lowest({"Ana": [7, 8, 6], "Luis": [4, 3, 5]})
        ('Ana', 7.0, 'Luis', 4.0)
    """
    if not data:
        raise ValueError("The class needs at least one student.")

    # Use the first student as the starting point for both averages.
    students = list(data.items())
    name, marks = students[0]
    highest = calculate_student_average(marks)
    lowest = highest
    highest_name = name
    lowest_name = name

    # Compare the remaining students with the current highest and lowest.
    for name, marks in students[1:]:
        average = calculate_student_average(marks)

        if average > highest:
            highest = average
            highest_name = name

        if average < lowest:
            lowest = average
            lowest_name = name

    return highest_name, highest, lowest_name, lowest
