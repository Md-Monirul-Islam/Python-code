import os.path
for file in [__file__,os.path.dirname(__file__),'/','./broken_link']:
    print("File             :",file)
    print("Absolute          :",os.path.isabs(file))
    print("Is file?         :",os.path.isfile(file))
    print("Is Dir?          :",os.path.isdir(file))
    print("Is Link?          :",os.path.islink(file))
    print("Exits               :",os.path.exists(file))
    print("Link exists          :",os.path.lexists(file))