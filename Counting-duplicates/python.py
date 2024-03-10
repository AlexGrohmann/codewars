# def duplicate_count(text):
#     count = 0
#     chars_lower = []
#     chars_upper = []
#     for char in text:
#         if char.isupper() and char not in chars_upper:
#             chars_upper.append(char)
#         if char.islower() and char not in chars_lower:
#             chars_lower.append(char)

#     for x in chars_lower:
#         x_count = text.count(x)
#         if x_count > 1:
#             count = count + 1
#     for x in chars_upper:
#         x_count = text.count(x)
#         if x_count > 1:
#             count = count + 1
#     return count


def duplicate_count(text):
    text_lower = text.lower()
    count = 0
    chars = []
    for char in text_lower:
        if char not in chars:
            chars.append(char)
    for elem in chars:
        char_count = text_lower.count(elem)
        if char_count > 1:
            count = count + 1
    return count


print(duplicate_count(""), 0)
print(duplicate_count("abcde"), 0)
print(duplicate_count("abcdeaa"), 1)
print(duplicate_count("abcdeaB"), 2)
print(duplicate_count("Indivisibilities"), 2)
print(duplicate_count("o9V0hSe9LfgqnSFFmUyfOegkT7ptEkcrXhJkYlF9EEOGuU8CjpUQlAN"), 17)
print(duplicate_count("KYK1rEE8xOP"), 2)
