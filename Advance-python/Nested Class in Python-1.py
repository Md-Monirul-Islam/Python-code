class Army:                                              #outer class
    def __init__(self):                                  #constructor
        self.name = "MD.Monirul Islam"
        self.gun = self.Gun()                            #creating inner class object
    def show(self):                                      #instance method
        print("Name->>",self.name)
    class Gun:                                           #inner class
        def __init__(self):
            self.name = "AK47"
            self.capacity = "75 Rounds"
            self.length = "34.3 inch"
        def display(self):
            print("Gun name",self.name)
            print("Gun capacity",self.capacity)
            print("Gun length",self.length)

Group = Army()
print(Group.name)
Group.show()
print(Group.gun.name)
print(Group.gun.display())
print(Group.gun)

g = Group.Gun
print(Group.name)

