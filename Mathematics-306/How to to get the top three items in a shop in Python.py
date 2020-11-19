from heapq import nlargest
from operator import itemgetter
items = {
    "item1>>":120,
    "item2>>":239,
    "item3>>":354,
    "item4>>":567,
    "item5>>":679,
    "item6>>":110,
}
for name,value in nlargest(3,items.items(),key=itemgetter(1)):
    print(name,value)