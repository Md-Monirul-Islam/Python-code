dic = {1:10,2:20,3:30,5:50,7:70}
def is_key_present(x):
    if x in dic:
        print("This key already exists in dictionary.")
    else:
        print("Key is not in dictionary.")
is_key_present(1)
is_key_present(4)