#static method without parameter
class Mobile:
    identity = "YES"                                      #class variable
    @staticmethod                                         #decorator
    def show_model():                                     #static method
        print("match identity??",Mobile.identity)
Nokia = Mobile()
Mobile.show_model()                                       #calling static method
