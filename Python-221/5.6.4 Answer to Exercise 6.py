a = tuple([1,1,2,3,3])
b = list(a)
print(len(b))
c = set(b)
print(len(c))
d = list(c)
print(len(d))
e = list(range(1,12))
dictionary = {
    "Jane Doe": "+27 555 5367 ",
    "John Smith": "+27 555 6254",
    "Bob Stone": "+27 555 5689",
}
t = list(dictionary.items())
v = list(dictionary.values())
k = list(dictionary)
s = "antidisestablishmentarianism"
s2 = "".join(sorted(s))
w = "the quick brown fox jumped over the lazy dog".split()
print(w)
print(s2)
print(t)
print(k)