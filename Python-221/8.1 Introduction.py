def my_function():
     my_other_function()

def my_other_function():
    print("Hello!")
# this is fine, because my_other_function is now defined
my_function()


def my_function():
    my_other_function()


def my_another_function():
    print("World!")


# this is not fine, because my_other_function is now defined
my_function()