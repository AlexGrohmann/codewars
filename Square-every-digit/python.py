def square_digits(num):
    string = str(num)
    result = ""
    for x in string:
        result += str(int(x) * int(x))
    return int(result)
