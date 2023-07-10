def solution(s):
    inputArray = [*s]
    if len(inputArray) % 2 != 0:
        inputArray.append("_")

    result = []
    for i in range(0, len(inputArray), 2):
        result.append(inputArray[i] + inputArray[i + 1])

    return result


print(solution("abcdefg"))
print(solution("abcdef"))
