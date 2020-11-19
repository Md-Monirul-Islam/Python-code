class Mobile:
    def __init__(self):
        self.model = "Nokia 2"
    def get_model(self):
        return self.model
Nokia = Mobile()
print(Nokia.get_model())