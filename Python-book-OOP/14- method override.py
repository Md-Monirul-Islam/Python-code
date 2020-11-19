class Thought(object):
    def __init__(self):
        pass
    def message(self):
        print('I am a JUSTian')
class advice(Thought):
    def __init__(self):
        super(advice,self).__init__()
    def message(self):
        print('I am a CSEian')
obj = Thought()
obj.message()
obj_1 = advice()
print(issubclass(advice,Thought))