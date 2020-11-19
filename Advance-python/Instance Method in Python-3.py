class Mobile:
    def __init__(self):
        self.model = "Nokia 2"
    def show_model(self,price):
        self.price = price
        print("Model",self.model,"price",self.price)
Nokia = Mobile()
Nokia.show_model(10000)