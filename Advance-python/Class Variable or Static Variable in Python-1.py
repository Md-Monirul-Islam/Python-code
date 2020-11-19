class Color:
    choice = "Green"
    @classmethod
    def is_choice(cls):
        print(cls.choice)
object = Color()
print(Color.choice)
object.is_choice()