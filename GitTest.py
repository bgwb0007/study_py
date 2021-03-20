import itertools

data = [1,2,3,4,5]

for i in itertools.combinations(data,3):
    print(list(i))