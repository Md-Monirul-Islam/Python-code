#classmethod with parameter
class Mobile:
    identity = "YES"
    @classmethod                                           #decorator
    def show_model(cls,ram):                               #class method
        cls.ram = ram
        print("matched identity??",cls.identity)
        print("RAM",cls.ram)
Nokia = Mobile()
Nokia.show_model("4GB")                                    # calling class method