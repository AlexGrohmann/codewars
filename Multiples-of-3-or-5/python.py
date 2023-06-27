def solution(number):
    result = 0
    for x in range(number):
        if x % 3 == 0 or x % 5 == 0:
            result += x
    print(result)
    return result


solution(50)
