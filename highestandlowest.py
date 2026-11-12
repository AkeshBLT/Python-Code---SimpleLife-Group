
def find_highest_and_lowest(data):
    """
    Find the highest and lowest student averages.

    Args:
        data: A non-empty list of students with names
              and their test marks (between 0 and 10).

    Returns:
        The names and average grades of the students
        with the highest and lowest averages.
    """
    name, marks = data[0]

    highest = calculate_student_average(marks)
    lowest = highest
    highest_name = name
    lowest_name = name

    for name, marks in data:
        average = calculate_student_average(marks)

        if average > highest:
            highest = average
            highest_name = name

        if average < lowest:
            lowest = average
            lowest_name = name

    return highest_name, highest, lowest_name, lowest
