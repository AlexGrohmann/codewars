def to_camel_case(text):
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
