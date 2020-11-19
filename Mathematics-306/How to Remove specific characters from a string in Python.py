def strip_string(str,char):
    return ''.join(c for c in str if c not in char)
print(strip_string("I love my country","mue"))