class Rectangle:
    w = []
    h = []

    def __init__(self, width, height):
        self.width = width
        self.w.append(width)
        self.height = height
        self.h.append(height)

    # def area(self):
    #     return self.height * self.width

    @staticmethod
    def area(width, height):
        return width * height

    @classmethod
    def instances(cls):
        num = len(cls.w)
        for i in range(num):
            print(cls.w[i] * cls.h[i])


class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)


r1 = Rectangle(3, 4)
r2 = Rectangle(5, 4)
s = Square(3)
print(Rectangle.area(8, 7))
Rectangle.instances()
