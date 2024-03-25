def alphabet_position(text):
    alphabet = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
    ]
    result = ""
    for char in text:
        if char.isalnum():
            result = result + " " + str(alphabet.index(char.lower()) + 1)
    return result.strip()


def alphabet_position_fancy(text):
    return " ".join(str(ord(c) - 96) for c in text.lower() if c.isalpha())
