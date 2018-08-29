"""Exercise 2."""

num1 = 45
num2 = 50
num3 = 14


def mean(num1, num2):
    """Calculates the mean between two numbres."""
    return (num1 + num2)/2


mean = mean(num1, num2)


def biggest(num1, num2, num3):
    """Computes the bigger value among three numbers."""
    biggest = num1
    if num2 > biggest:
        biggest = num2
    elif num3 > biggest:
        biggest = num3
    return biggest


print("The mean between %.2f and %.2f is %.2f" % (num1, num2, mean))
print("Among %.2f, %.2f e %.2f, the biggest is %.2f" % (num1, num2, num3,
      biggest(num1, num2, num3)))
