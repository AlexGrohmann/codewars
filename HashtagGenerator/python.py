def generate_hashtag(s):
    result = "#"
    words = s.split(" ")
    for x in words:
        result = result + x.capitalize()

    if (len(result) == 1 or len(result) > 140):
        return False
    else:
        return result


print(generate_hashtag(""), False)
print(generate_hashtag(" "), False)
print(generate_hashtag("Do We have A Hashtag"), "#DoWeHaveAHashtag")
print(generate_hashtag("Codewars"), "#Codewars")
print(generate_hashtag("Codewars Is Nice"), "#CodewarsIsNice")
print(generate_hashtag("Codewars is nice"), "#CodewarsIsNice")
print(generate_hashtag("code" + " " + "wars"), "#CodeWars")
print(
    generate_hashtag(
        "Looooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooong Cat"
    ),
    False
)
print(generate_hashtag("a"), "#A" + "a")
print(generate_hashtag("a"), False)
