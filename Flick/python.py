def flick_switch(lst):
    result = []
    state = True
    for item in lst:
        if item == "flick":
            state = not state
            result.append(state)
        else:
            result.append(state)
    return result
