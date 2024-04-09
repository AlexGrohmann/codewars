def to_camel_case_first_try(text):
    result = ""
    upperLetterNext = False
    for x in range(len(text)):
        if text[x] == "-" or text[x] == "_":
            upperLetterNext = True
        else:
            if upperLetterNext:
                result = result + text[x].upper()
                upperLetterNext = False
            else:
                result = result + text[x]
    return result


def to_camel_case(text):
    removed = text.replace("-", " ").replace("_", " ").split()
    if len(removed) == 0:
        return ""
    return removed[0] + "".join([x.capitalize() for x in removed[1:]])


print(to_camel_case(""), "", "An empty string was provided but not returned")
print(
    to_camel_case("the_stealth_warrior"),
    "theStealthWarrior",
    "to_camel_case('the_stealth_warrior') did not return correct value",
)
print(
    to_camel_case("The-Stealth-Warrior"),
    "TheStealthWarrior",
    "to_camel_case('The-Stealth-Warrior') did not return correct value",
)
print(
    to_camel_case("A-B-C"), "ABC", "to_camel_case('A-B-C') did not return correct value"
)
