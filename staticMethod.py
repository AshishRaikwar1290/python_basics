class Math:
    def __init__(self, num):
        self.num = num

    def add_to_num(self, n):
        self.num = self.num + n

    @staticmethod
    def add(a, b):
        return a + b

a = Math(5)
print(a.num)
a.add_to_num(6)
print(a.add(5, 6))
print(Math.add(3, 4))