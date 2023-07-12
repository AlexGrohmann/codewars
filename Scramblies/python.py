from collections import Counter


def scramble(s1, s2):
    cnt = Counter(s1)
    cnt.subtract(Counter(s2))
    return (all(e >= 0 for e in cnt.values()))


print(scramble('rkqodlw', 'world'))
print(scramble('cedewaraaossoqqyt', 'codewars'))
print(scramble('katas', 'steak'))
print(scramble('scriptjava', 'javascript'))
print(scramble('scriptingjava', 'javascript'))
