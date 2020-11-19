class Mobile:
    indentity = "match"  # class variable
    def __init__(self):
        self.model = "Nokia 2"  # instance variable
    def show_model(self):       # instance method
        print("Model=>",self.model) # accessing intance variable
    @classmethod
    def is_indentity(cls):     # class method
        print("finger print identity",cls.indentity)  # accessing class variable
Nokia = Mobile()
print(Nokia.indentity)
print(Nokia.model)
Nokia.show_model()
Mobile.indentity = "No"
Nokia.is_indentity()