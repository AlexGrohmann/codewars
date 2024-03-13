def get_middle(s):
    if len(s) % 2 == 0:
        middle = int(len(s) / 2)
        return s[middle - 1] + s[middle]
    else:
        middle = int(len(s) / 2)
        return s[middle]
