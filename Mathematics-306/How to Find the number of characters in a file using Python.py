import collections
import pprint
File_input = input("File name :")
with open(File_input,"r") as info:
    count = collections.Counter(info.read().upper())
    value = pprint.pformat(count)
print(value)