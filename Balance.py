class Balance:
    def __init__(self):
        self.right = 0
        self.left = 0

    def add_right(self, w):
        self.right += w

    def add_left(self, w):
        self.left += w

    def result(self):
        if self.right == self.left:
            return '='
        if self.right > self.left:
            return 'R'
        return 'L'
