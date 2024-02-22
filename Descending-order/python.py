def descending_order(num):
    result = []
    for d in str(num):
        result.append(int(d))
    result.sort(reverse=True)
    return int("".join(str(i) for i in result))
