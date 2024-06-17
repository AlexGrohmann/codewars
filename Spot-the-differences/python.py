def spot_diff(s1, s2):
    result = []
    for i in range(len(s1)):
        if s1[i] != s2[i]:
            result.append(i)
    return result
