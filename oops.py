# class Person:
#     name = "Ashish"
#     occupation = "Software Developer"
#     networth = 10
#     def info(self):
#         print(f'{self.name} is a {self.occupation}')

# a = Person()
# a.name = "Shubham"
# a.occupation = "Accountant"

# b = Person()
# b.name = "Nikita"

# print(a.name, a.occupation)
# a.info()
# b.info()

#construtor

# class Person:
#     def __init__(self, n, o):
#         self.name = n
#         self.occ = o

#     def info(self):
#         print(f'{self.name} is a {self.occ}')

# a = Person("Ashish", "Frontend")
# b = Person("Divya", "UI")

# a.info()
# b.info()

#decorators
def greet(fx):
    def mfx(*args, **kwargs):
        print("good morning")
        fx(*args, **kwargs)
        print("Thansk for using me")
    return mfx
@greet
def hello():
    print("hello world")

@greet
def add(a, b):
    print(a+b)

hello()
add(2, 3)


    
