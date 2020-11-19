''''
1. Rewrite the program from the ﬁrst question of exercise 2
so that it prints the text of Python’s original exception
inside the except clause instead of a custom message.
'''
person = {}
poperties = [
    ("Name",str),
    ("surname",str),
    ("Age",int),
    ("height",float),
    ("weight",float)
]
for property,p_type in poperties:
    valid_value = None
    while valid_value is None:
        try:
            value = input("Please enter your %s: "%property)
            valid_value = p_type(value)
        except ValueError as ve:
            print(ve)