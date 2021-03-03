class calc:
    def __init__(self, a, b):
        self.num1 = float(a)
        self.num2 = float(b)

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2
