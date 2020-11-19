list1 = ['a','b','c','d','e','f','g','h','i','j']
def list_slice(S,step):
    return [S[i::step] for i in range(step)]
print(list_slice(list1,5))