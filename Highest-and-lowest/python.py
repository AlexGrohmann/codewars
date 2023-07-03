def high_and_low(numbers):
    split = numbers.split(" ")
    maxValue = int(float(numbers[0]))
    minValue = int(float(numbers[0]))
    for x in range(len(split)):
        if int(float(split[x])) > maxValue:
            maxValue = int(float(split[x]))
        if int(float(split[x])) < minValue:
            minValue = int(float(split[x]))
    print(str(maxValue) + " " + str(minValue))
    return str(maxValue) + " " + str(minValue)


high_and_low("8 3 -5 42 -1 0 0 -9 4 7 4 -4")
high_and_low("-1 -1")
