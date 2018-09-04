"""Operations over a list of numbers."""


def biggest(a_list):
    """Return a list with index and the biggest number in a list."""
    # Return [index, biggest]
    # For example: given the list [1,100,33], returns [1, 100]
    biggest_number = a_list[0]
    i = 0
    index = 0
    while i < len(a_list):
        if a_list[i] > biggest_number:
            biggest_number = a_list[i]
            index = i
        i += 1
    return [index, biggest_number]


def smallest(a_list):
    """Return a list with index and the smallest number in a list."""
    # Return [index, smallest]
    # For example: given the list [1,100,33], returns [0, 1]
    smallest_number = a_list[0]
    i = 0
    index = 0
    while i < len(a_list):
        if a_list[i] < smallest_number:
            smallest_number = a_list[i]
            index = i
        i += 1
    return [index, smallest_number]


def sum_of_even(a_list):
    """Return the sum of even numbers in a list."""
    sum = 0.0
    i = 0
    while i < len(a_list):
        if a_list[i] % 2 == 0:
            sum += a_list[i]
        i += 1
    return sum


def sum_of_odd(a_list):
    """Return the sum of odd numbers in a list."""
    sum = 0.0
    i = 0
    while i < len(a_list):
        if a_list[i] % 2 != 0:
            sum += float(a_list[i])
        i += 1
    return sum


def division_of_sum(a_list):
    """Return the sum of the even divided by sum of the odd."""
    even = sum_of_even(a_list)
    odd = sum_of_odd(a_list)
    if odd == 0 or (even == 0 and odd == 0):
        return "Division by zero"
    else:
        return float(even)/odd


def get_inverse(a_list):
    """Return the inverse order of a list of numbers."""
    inverse_list = []
    i = len(a_list)
    while i > 0:
        inverse_list.append(a_list[i - 1])
        i -= 1
    return inverse_list
