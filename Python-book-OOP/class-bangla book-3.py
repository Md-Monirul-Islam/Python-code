class Monster(object):
    identity = 'negative character'

    def __init__(self,head,color):
        self.head = head
        self.color = color

    def attack(self):
        print("just attack Hero, Mu......hahahahaha")

mournsnale = Monster(5,'Black')
tangleface = Monster(6,'Yollow')

print("I have a " + str(mournsnale.head) + " headed",mournsnale.identity)
print("I have a " + str(tangleface.head) + " haeded",tangleface.identity)