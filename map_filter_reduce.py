from functools import reduce

def cube(x):
    return x*x*x


l = [1, 2, 3, 4]

newlist = list(map(cube, l))
print(newlist)


newFilterList = list(filter(lambda x: x>=2, l))
print(newFilterList)

sum = reduce(lambda x, y: x+y, l)

print(sum)