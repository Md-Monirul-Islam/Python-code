class myclass:
    classy = '\"main value\"'
dd = myclass()
print(dd.classy)
dd.classy = '\"sub value\"'
print(dd.classy)
del dd.classy
print(dd.classy)