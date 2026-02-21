# lists
from doctest import OutputChecker


marks = [3, 5, 6, "", True]


if 7 in marks:
    print("Yes")
else:
    print("No")
    
    
print(marks)

lst = [i for i in range(4)]
print(lst)


# output
# No
# [3, 5, 6, '', True]
# [0, 1, 2, 3]


# list methods

l = [11, 45, 1, 6, 4]
print(l)
l.append(7)
l.sort(reverse=True)
l.reverse()
print(l)
print(l.index(1))
print(l.count(1))
m = l.copy()
m[0] = 0
l.insert(1, 899)
m = [900, 1000, 1100]
k = l+m
print(k)
l.extend(m)
print(l)

# Output

# [11, 45, 1, 6, 4]
# [1, 4, 6, 7, 11, 45]
# 0
# 1
# [1, 899, 4, 6, 7, 11, 45, 900, 1000, 1100]
# [1, 899, 4, 6, 7, 11, 45, 900, 1000, 1100]