class person:
    def __init__(self,name):
        self.name = name
    def sayhello(self):
        print('Hello, my name is',self.name)
    def __del__(self):
        print('%s says bye.'%self.name)
A = person('Munna')