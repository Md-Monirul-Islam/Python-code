''''
2. Rewrite the second program from exercise 2 so that it uses
this logging conﬁguration instead of printing messages to the console (except for the ﬁrst
print statement, which is the purpose of the function
'''
import logging
def print_list_element(thelist, index):
    try:
        print(thelist[index])
    except IndexError:
        logging.error("The list has no element at index %d." % index)