class Animal:
    def eat(self):
        print("Animal eats food")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")


# Create object
p = Puppy()

p.eat()    # from Animal
p.bark()   # from Dog
p.weep()   # from Puppy