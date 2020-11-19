x = 'TutarialPoint'
y = b'TutarialPoint'
z = x.encode('ASCII')
if (z==y):
    print('encoding successfull.')
else:
    print('encoding unseccussfull.')


z = y.decode('ASCII')
if (z==x):
    print('decoding successfull.')
else:
    print('decoding unsuccessfull.')