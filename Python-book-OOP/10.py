class MyDict(dict):

    def __setitem__(self, key, val):
        print('setting a key and value!')
        dict.__setitem__(self, key, val)


dd = MyDict()
dd['a'] = 10
dd['b'] = 20

for key in dd.keys():
    print('{0}={1}'.format(key, dd[key])) 