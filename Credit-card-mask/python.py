# return masked string
def maskify(cc):
    if len(cc) > 4:
        result = ""
        for _ in range(len(cc) - 4):
            result = result + "#"
        result = result + cc[len(cc) - 4 :]
        return result
    return cc
