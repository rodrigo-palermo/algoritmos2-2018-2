"""Gives information about the parity of a list o numbers."""


def is_even(a_list):
    """Return True if a number in a list is even. Otherwise, returns False."""
    item = 0
    parity_list = []
    while item < len(a_list):
        if a_list[item] % 2 == 0:
            parity_list.append(True)
        else:
            parity_list.append(False)
        item += 1
    return parity_list
