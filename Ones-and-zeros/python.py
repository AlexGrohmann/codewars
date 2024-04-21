def binary_array_to_number(arr):
    total = 0
    i = 1
    for num in arr[::-1]:
        total += i * num
        i *= 2
    return total


print(binary_array_to_number([0, 0, 1, 0]), 2)
print(binary_array_to_number([0, 0, 0, 1]), 1)
print(binary_array_to_number([0, 1, 1, 0]), 6)
print(binary_array_to_number([1, 1, 1, 1]), 15)
