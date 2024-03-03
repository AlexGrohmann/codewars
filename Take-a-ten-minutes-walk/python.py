def is_valid_walk(walk):
    vertical_walk = walk.count("n") == walk.count("s")
    horizontal_walk = walk.count("e") == walk.count("w")
    length = len(walk) == 10
    return vertical_walk and horizontal_walk and length
