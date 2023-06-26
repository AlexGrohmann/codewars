def sum_digits(number):
    number = abs(number)
    strr = str(number)
    list_of_number = list(map(int, strr.strip()))
    return sum(list_of_number)


sum_digits(-51)
