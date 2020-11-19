''''
1. Modify the example above to include type conversion of the properties:
age should be an integer, height and weight
should be ﬂoats, and name and surname should be strings.
'''
Person = {}
poperties = [
    ("Name",str),
    ("Surname",str),
    ("Age",int),
    ("Height",float),
    ("Weight",float)
]
for prop,p_type in poperties:
    Person[prop] = p_type(input("Please enter your %s: " %prop))