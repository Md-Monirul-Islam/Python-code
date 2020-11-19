class person:
    def speak(self):
        print('I can speak English.')
class man(person):
    def text(self):
        print('I can write a Message.')
class woman(person):
    def call(self):
        print('I can send a miss call.')
man = man()
man.text()
man.speak()