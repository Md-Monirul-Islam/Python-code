class Mobile:
    def __init__(self):
        self.model = "Nokia 2"

    def set_model(self):
        self.model = "Samsung A50"
Nokia = Mobile()
print(Nokia.model)

Samsung = Mobile()
Samsung.set_model()
print(Samsung.model)