class Employee:
    def __init__(self):
        self.__name = "Harry"

a = Employee()
# print(a.name)

# print(a.__name)

# name mangling
print(a._Employee__name)


# __ for private
# _ for protected