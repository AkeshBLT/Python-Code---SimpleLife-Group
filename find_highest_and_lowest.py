from calculate_student_average import calculate_student_average


def find_highest_and_lowest(
    data: dict[str, list[float]]
) -> str:

    if not data:
        raise ValueError("The class needs at least one student.")

    # Use the first student as the starting point for both averages.
    students = list(data.items())
    name, marks = students[0]
    highest = calculate_student_average(data, name)
    lowest = highest
    highest_name = name
    lowest_name = name

    # Compare the remaining students with the current highest and lowest.
    for name, marks in students[1:]:
        average = calculate_student_average(data, name)

        if average > highest:
            highest = average
            highest_name = name

        if average < lowest:
            lowest = average
            lowest_name = name


    return (f"Highest average: {highest_name} ({highest:.1f})\n"
            f"Lowest average: {lowest_name} ({lowest:.1f})")
