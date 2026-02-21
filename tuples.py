tup = (1, 5, 6)
print(type(tup), tup)

tup = (1,)
print(type(tup), tup)

# we cannot change tuples

if 1 in tup:
    print("yes")
    
tup2 = tup[1:4]
print(tup2)

# output
# <class 'tuple'> (1, 5, 6)
# <class 'tuple'> (1,)
# yes
# ()


countries = ("Spain", "Italy", "India")
temp = list(countries)
temp.append("Russia")
temp.pop(2)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)

# addition 
countries = ("india",)
countries2 = ("us",)
add = countries + countries2
print(add)

tuple1 = (0, 1, 2, 3, 2, 31, 1, 3, 2, 3)
# res = tuple1.count(3)
# res = tuple1.index(3)
res = tuple1.index(3, 4, 8)
print(res)

# output
# ('Spain', 'Italy', 'Finland')
# ('india', 'us')
# 7