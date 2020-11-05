class OddEvenSeparator:
    def __init__(self):
        self.odd = []
        self.even = []

    def add_number(self, num):
        if num % 2 == 0:
            self.even.append(num)
        else:
            self.odd.append(num)

    def even(self):
        return self.even

    def odd(self):
        return self.odd
