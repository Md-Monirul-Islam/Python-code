""""
without parameter
"""

class Mobile:
    def __init__(self):
        self.model = "Nokia 2"     #instance variable
    def show_model(self):          # instance method
        print("Model=>>",self.model)  #accessing instance variable
Nokia = Mobile()
Nokia.show_model()
print(Nokia.model)