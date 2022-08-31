max_size = 50
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def __str__(self):
        return 'Rectangle(width=%d, height=%d)' % (self.width, self.height)
    def set_width(self, width):
        self.width = width
    def set_height(self, height):
        self.height = height
    def get_area(self):
        return self.width * self.height
    def get_perimeter(self):
        return 2*self.width + 2*self.height
    def get_diagonal(self):
        return ((self.width ** 2 + self.height ** 2) ** 0.5)
    def get_picture(self):
        if self.width > max_size or self.height > max_size:
            return "Too big for picture."
        else:
            # TODO: print the rectangle using *
            rectangle = ''
            for i in range(self.height):
                rectangle += '*' * self.width + '\n'
            return rectangle
    def get_amount_inside(self, shape):
        # shape can be either square or rectangle.
        # return the amount of times shape can be fit inside self without rotations
        times = 0
        for i in range(round(self.height / shape.height)):
            times += round(self.width / shape.width)
        return times



class Square(Rectangle):
    def __init__(self, length):
        super().__init__(length, length)
    def __str__(self):
        return 'Square(side=%d)' % (self.width)
    def set_side(self, side):
        self.width = side
        self.height = side
    def set_height(self, height):
        self.set_side(height)
    def set_width(self, width):
        self.set_side(width)

