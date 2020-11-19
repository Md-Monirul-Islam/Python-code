class C:
    def show(self):
        print('You can see me.')
    def _Notshow(self):  #under score means private method.
        print('You can not see me.')
C().show()
C()._Notshow()