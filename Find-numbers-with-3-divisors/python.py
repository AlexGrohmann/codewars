from math import isqrt as sq


def solution_fancy(n, m):  # 16 81
    a, b = sq(sq(n)), sq(sq(m))
    print(sq(n), sq(m), a, b)
    if a**4 < n:
        a += 1
    return [i**4 for i in range(a, b + 1) if is_prime(i)]


def is_prime(x):
    for i in range(2, sq(x) + 1):
        if x % i == 0:
            return False
    return True


def solution_timeout(n, m):  # 2 20
    result = []
    for x in range(n, m):  # von 3 bis 19
        divisors = 0
        for z in range(x - 1):  # zahl zwischen 0 und der zahl zwischen 3 und 19
            if x > 1 and z > 1 and x % z == 0:
                divisors = divisors + 1
        if divisors == 3:
            result.append(x)
    return result


def solution(n, m):
    return [
        x**4
        for x in range(*[int(-(-(x ** (1 / 4)) // 1)) for x in (n, m + 1)])
        if next((0 for i in range(2, int(x**0.5) + 1) if not x % i), 1 < x)
    ]


# print(solution(2, 100), [16, 81])
# print(solution(10000, 100000), [14641, 28561, 83521])
# print(solution(624, 625), [625])
# print(solution(625, 626), [625])
# print(solution(734, 735), [])

print(solution_fancy(2, 100), [16, 81])
