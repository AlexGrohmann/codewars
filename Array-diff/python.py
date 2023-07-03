def array_diff(a, b):
    result = []
    if (len(b) == 0):
        return a
    for x in range(len(a)):
        setValue = 0
        for y in range(len(b)):
            if (a[x] == b[y]):
                setValue = 1

        if (setValue != 1):
            result.append(a[x])
    print(result)


array_diff([1, 2, 3], [1, 2])
array_diff([1, 2, 2], [1])
array_diff([1, 2, 2], [2])
array_diff([1, 2, 2], [])
array_diff([1, 2, 3], [1, 2])
