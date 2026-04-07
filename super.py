class Parent:
    def parent(self):
        print("i am parent")

class Child(Parent):
    def child(self):
        super().parent()
        print("i am child")

child_obj = Child()
child_obj.child()