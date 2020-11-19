dictionary = {
    "Jane Doe": "+27 555 5367 ",
    "John Smith": "+27 555 6254",
    "Bob Stone": "+27 555 5689",
}
dictionary["Jane Doe"] = "+27 555 1024"
dictionary["Anna Cooper"] = "+27 555 3237"
print(dictionary["Bob Stone"])
print(dictionary.get("Bob Stone",None))
print(dictionary.keys())
print(dictionary.values())
