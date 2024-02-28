def find_short(s):
    words = s.split(" ")
    l = len(words[0])
    for word in words:
        if len(word) < l:
            l = len(word)
    return l


def find_short_fancy(s):
    return min(len(x) for x in s.split())
