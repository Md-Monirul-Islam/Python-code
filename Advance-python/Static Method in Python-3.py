#static method with parameter
class Mobile:
    @staticmethod
    def show_model(model,price):
        a = model
        b = price
        print("Model=>>",model,",","Price=>>",price)
Nokia = Mobile()
Mobile.show_model("Nokia 2",9500)