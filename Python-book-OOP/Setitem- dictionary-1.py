class mydict(dict):
    def __setitem__(self, key, value):
        print('setting a key and value!')
        dict.__setitem__(self,key,value)
dd = mydict()
dd['a'] = 10
dd['b'] = 20
dd['c'] = 30
for key in dd.keys():
    print('{0} = {1} '.format(key,dd[key]))

