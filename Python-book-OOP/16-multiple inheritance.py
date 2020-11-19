class Mother:
    pass
class Father:
    pass
class Child(Mother,Father):
    pass
print(issubclass(Child,Mother) and issubclass(Child,Father))