def cube_checker(volume, side):
    if volume < 1:
        return False
    if side < 1:
        return False
    return (volume / side / side / side) == 1
