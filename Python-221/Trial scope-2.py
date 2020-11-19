print(range(20))
print(list(range(20)))
animuls = ['cat','dog','cow','horse']
for first_animul in animuls:
    for second_animul in animuls:
        print("Yesterday I bought a %s. Today I bought a %s." % (first_animul,second_animul))

import itertools
for i in itertools.count(1):
    print(i)  #1, 2, 3....

for i in itertools.count(1, 0.5):
    print(i) # 1.0, 1.5, 2.0....
for animal in itertools.cycle(['cat', 'dog']):
    print(animal) # 'cat', 'dog', 'cat', 'dog'..

for i in zip(range(5), range(5, 10), range(10, 15)):
    print(i)
