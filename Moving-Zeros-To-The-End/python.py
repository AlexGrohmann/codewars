def move_zeros(lst):
    zero_count = 0
    result = []
    for item in lst:
        if item == 0:
            zero_count = zero_count + 1
        else:
            result.append(item)
    for _ in range(zero_count):
        result.append(0)
    print(result)
    return result


move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1])
