def word_search(query, seq):
    result = [str for str in seq if query.lower() in str.lower()]
    if len(result) == 0:
        return ["None"]
    else:
        return result


# Test cases
print(word_search("aB", ["za", "ab", "abc", "zab", "zbc"]))  # ["ab", "abc", "zab"]
print(word_search("ab", ["za", "ab", "abc", "zab", "zbc"]))  # ["ab", "abc", "zab"]
print(word_search("ab", ["za", "aB", "Abc", "zAB", "zbc"]))  # ["aB", "Abc", "zAB"]
print(word_search("abcd", ["za", "aB", "Abc", "zAB", "zbc"]))  # ["Empty"]
