"""Find the number in the middle."""

# number_list = [3, 1, 2]


def greatest(a_list):
    """Return the greatest number in a list."""
    greatest_number = a_list[0]
    for number in a_list:
        if number > greatest_number:
            greatest_number = number
    return greatest_number


def smallest(a_list):
    """Return the greatest number in a list."""
    smallest_number = a_list[0]
    for number in a_list:
        if number < smallest_number:
            smallest_number = number
    return smallest_number


def middle(a_list):
    """Return the number in the middle in a list of 3 numbers."""
    greatest_number = greatest(a_list)
    smallest_number = smallest(a_list)
    i = 0
    middle_number = a_list[i]
    while middle_number == greatest_number or middle_number == smallest_number:
        i += 1
        middle_number = a_list[i]
    return middle_number

# print(middle(number_list))
