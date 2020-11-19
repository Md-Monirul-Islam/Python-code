# classmethod without parameter
class Mobile:
    @classmethod                #decorator
    def show_model(cls):        # classmethod
        print("Nokia 2")
Nokia = Mobile()
Nokia.show_model()              #calling classmethod