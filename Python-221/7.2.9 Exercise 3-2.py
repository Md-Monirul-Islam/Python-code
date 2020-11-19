''''
2. Rewrite the program from the second question of exercise
2 so that the exception which is caught in the except
clause is re-raised after the error message is printed.
'''
def print_list_element(thelist, index):
    try: print(thelist[index])
    except IndexError as ie:
        print("The list has no element at index %d." % index)
        raise ie