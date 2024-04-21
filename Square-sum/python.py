def square_sum(numbers):
    result = 0
    for x in numbers:
        result = result + x**2
    return result


def square_sum_fancy(numbers):
    return sum(x**2 for x in numbers)
