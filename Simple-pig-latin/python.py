def pig_it(text):
    list = text.split()
    result = ""
    for item in list:
        if not item.isalnum():
            result += item
        else:
            result += item[1:] + item[0] + "ay "
    return result.strip()
