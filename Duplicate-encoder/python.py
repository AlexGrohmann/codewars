def duplicate_encode(word):
    result = ""
    for char in word:
        if word.lower().count(char.lower()) > 1:
            result = result + ")"
        else:
            result = result + "("
    return result


print(duplicate_encode("recede"), "()()()")
print(duplicate_encode("din"), "(((")
print(duplicate_encode("Success"), ")())())", "should ignore case")
print(duplicate_encode("(( @"), "))((")
