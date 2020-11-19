class SumList(object):
    def __init__(self, my_list):
        self.mylist = my_list
    def __add__(self, other):
        new_list = [x + y for x, y in zip(self.mylist, other.mylist)]

        return SumList(new_list)

    def __repr__(self):
        return str(self.mylist)


aa = SumList([3, 6, 9, 12, 15])

bb = SumList([100, 200, 300, 400, 500])
cc = aa + bb  # aa.__add__(bb)
print(cc)