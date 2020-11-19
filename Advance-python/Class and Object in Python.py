class Mobile(object):
    def __init__(self,model):
        self.model = model

    def show_model(self,price):
        self.price = price
        print("Model:",self.model,"\nprice:",self.price)
object = Mobile("Nokia 2")
object.show_model(10000)
print(id(object))