#         Parent
#        /      \
#    Child1   Child2

# One parent class is inherited by multiple child classes.

class Animal:
    def eat(self):
        print("Animal eats food")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Cat(Animal):
    def meow(self):
        print("Cat meows")


d = Dog()
d.eat()
d.bark()

c = Cat()
c.eat()
c.meow()


    #     A
    #    / \
    #   B   C
    #    \ /
    #     D
    # Combination of two or more types of inheritance (e.g., hierarchical + multiple)


class A:
    def showA(self):
        print("Class A")

class B(A):
    def showB(self):
        print("Class B")

class C(A):
    def showC(self):
        print("Class C")

class D(B, C):
    def showD(self):
        print("Class D")


obj = D()
obj.showA()
obj.showB()
obj.showC()
obj.showD()