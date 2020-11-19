try:
    age = int(input("Please enter your age: "))
except ValueError:
    print("Hey! That wasn't a number.")
else:
    print("I see that your are %d years old." %age)
finally:
    print("Really it was a good talking with you-goodbye.")