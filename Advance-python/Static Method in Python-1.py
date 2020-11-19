#static method without parameter
class Mobile:
    @staticmethod                   #decorator
    def show_model():               #static method
        print("Nokia 2")
Nokia = Mobile()
Mobile.show_model()                 #calling static method