"""Exercise Classe 4 - Item 2. User must insert 10 numbers."""

from sistema import *


def get_list():
    """Get 10 numbers typed by the user to construct a list."""
    i = 0
    list_num = []
    print("Type 10 numbers to calculate some operations: ")
    while i < 3:
        list_num.append(float(input(str(i+1)+": ")))
        i += 1
    return list_num


def list_operations():
    """Operations over the list."""
    a_list = get_list()
    biggest_number = biggest(a_list)
    smallest_number = smallest(a_list)
    sum_even = sum_of_even(a_list)
    sum_odd = sum_of_odd(a_list)
    division_sum = division_of_sum(a_list)
    inverted = get_inverse(a_list)

    return "The list: {}\n\
    Biggest number: {} (index {})\n\
    Smallest number: {} (index {})\n\
    Sum of the even numbers: {}\n\
    Sum of the odd numbers: {}\n\
    Division of sum (even/odd): {}\n\
    Inverse order list: {}\n\
    ".format(a_list, biggest_number[1], biggest_number[0], smallest_number[1],
             smallest_number[0], sum_even, sum_odd, division_sum, inverted)


print(list_operations())
