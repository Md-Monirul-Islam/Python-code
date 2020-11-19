class Monster:
    def __init__(self,color,head):
        self.color = color
        self.head = head

fogthing = Monster('Black',5)
mournsnake = Monster('Yellow',4)
tangleface = Monster('White',3)

print("I have " + str(fogthing.head) + " head and I\'m",fogthing.color)
print("I have " + str(mournsnake.head) + "head and I\'m",mournsnake.color)
print("I have " + str(tangleface.head) + "haed and I\'m",tangleface.color)
