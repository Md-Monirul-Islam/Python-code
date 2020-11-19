try:
    age = int(input("Please enter your age: "))
    if age < 0:
        raise ValueError("%d is not a valid age.only acept a possitive integer number." %age)
except ValueError as err:
    print("You entered incorrect age input: %s" %err)
else:
    print("I see that you are %d years old." % age)
