class Mobile:
    identity = "YES!"                            #class variable
    @classmethod
    def is_identit(cls):                         # class method
        print("Finger matched ?",cls.identity)   #accessing class variable
Nokia = Mobile()
Samsung = Mobile()
RealMe = Mobile()
print("Nokia",Nokia.identity)
Mobile.is_identit()
