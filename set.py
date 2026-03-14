s = {2, 4, 2, 6}
print(s)

# not {}
harry = set()
print(type(harry))

# output:
# {2, 4, 6}
# <class 'set'>


s = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}

print(s.union(s2))
print(s.intersection(s2))

# update the s
s.update(s2)

# update the s
s.intersection_update(s2)

# uncommon values
print(s.symmetric_difference(s2))

# symmetric_diffrence_update

# difference A-B
print(s.difference(s2))

print(s.isdisjoint(s2))

print(s.issuperset(s2))

print(s2.issubset(s))

# single item
s.add(5) 

s.remove(3)

# donot raise error
s.discard(3)


# pop item from back

# delete a set
del s

# clear set
s.clear()

# output
# {1, 2, 3, 4, 5, 6}
# {3, 4}
# set()
# set()
# False
# True
# True
# ERROR!
# Traceback (most recent call last):
#   File "<main.py>", line 42, in <module>
# NameError: name 's' is not defined

# === Code Exited With Errors ===