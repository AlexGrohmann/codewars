def high_and_low(numbers):
    numbers = numbers.split(" ")
    numbers = sorted(numbers, key=int)
    print(numbers[-1] + " " + numbers[0])
    return numbers[-1] + " " + numbers[0]


high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
high_and_low("-1 -1")
