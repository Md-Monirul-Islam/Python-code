str_1 = 'Hello world'
print(str_1.startswith('d'))

print(str_1.startswith('H'))

print(str_1.endswith('ld'))

print(str_1.find('H'))

print(str_1.find('lo'))

print(str_1.upper())

print(str_1.lower())

print(str_1.index('r'))

print(str_1.split())

print('*'.join(str_1))

s = ' how are you?'
s_1 = s.split()
print(s_1)
print('*'.join(s_1))

print(s.partition(' '))

print(str_1.partition(' '))

print(str_1.isprintable())

print(s.isalnum())

print(s.isnumeric())