class Monster:
    def __init__(self,name,color):
        self.name=name
        self.color=color

    def attack(self):
        print("just attacking......")

class Fogthing(Monster):
    def make_sound(self):
        print('Grrrrrrrrrrr\n')

class Mournsnake(Monster):
    def make_sound(self):
        print('Hiiiiisssssshhhhhhh\n')

fogthing = Fogthing('Fogthing','Black')
fogthing.attack()
fogthing.make_sound()
mournsnake = Mournsnake('Mournsnake','Yellow')
mournsnake.attack()
mournsnake.make_sound()
