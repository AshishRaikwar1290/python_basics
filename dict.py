dict = {
    344: "Harry",
    56: "Shubham"
}

print(dict[344])
print(dict.get(344))

print(dict.keys())
print(dict.values())

print(dict.items())

for key, value in dict.items():
    print(f"{key} {value}")

for key in dict.keys():
    print(dict[key])

# output
# Harry
# Harry
# dict_keys([344, 56])
# dict_values(['Harry', 'Shubham'])
# dict_items([(344, 'Harry'), (56, 'Shubham')])
# 344 Harry
# 56 Shubham
# Harry
# Shubham


ep1 = {122: 45, 123: 89, 567: 69, 670: 69}
ep2 = {222: 67, 566: 90}

ep1.update(ep2)
ep2.clear()
ep1.pop(122)

ep1.popitem()
# del ep1
del ep1[567]
print(ep1)

# {123: 89, 670: 69, 222: 67}



