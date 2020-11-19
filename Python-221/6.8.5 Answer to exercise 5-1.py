''''
1. Create a string which contains the ﬁrst ten positive integers separated
by commas and spaces. Remember that you can’t join numbers –
you have to convert them to strings ﬁrst. Print the output string.
'''

number_string = ", ".join(str(n) for n in range(1, 11))
print(number_string)