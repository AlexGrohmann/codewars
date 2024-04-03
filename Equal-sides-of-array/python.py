def find_even_index(arr):
    for i in range(0, len(arr)):
        LHS = sum(arr[:i])  # summe bis pos of i
        RHS = sum(arr[i + 1 :])  # summe ab i + 1
        if LHS == RHS:  # wenn beide summen gleich sind
            return i
    return -1
