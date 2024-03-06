def find_it(seq):
    for s in seq:
        if seq.count(s) % 2 != 0:
            return s
