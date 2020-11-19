class Monster(object):
    def __init__(self,color,head):
        self.color = color
        self.head = head


    def attack(self):
        print("just attack Hero, Mu.....hahahaha")

mournsnake = Monster('Black',5)
print("I am a " + str(mournsnake.head) + ' headed monster')
mournsnake.attack()