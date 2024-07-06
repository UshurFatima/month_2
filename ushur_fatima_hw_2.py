class Figure:
    unit = "cm"

    def __init__(self):
        pass

    def calculate_area(self):
        pass

    def info(self):
        pass


class Square(Figure):
    def __init__(self, side_length):
        super().__init__()
        self.__side_length = side_length

    def calculate_area(self):
        return self.__side_length ** 2

    def info(self):
        print(f"Square side length: {self.__side_length} {self.unit}, "
              f"area: {self.calculate_area()} {self.unit}")


class Rectangle(Figure):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width

    def calculate_area(self):
        return self.__length * self.__width

    def info(self):
        print(f"Rectangle length: {self.__length} {self.unit}, width: {self.__width} {self.unit}, "
              f"area: {self.calculate_area()} {self.unit}")


square1 = Square(5)
square2 = Square(8)

rectangle1 = Rectangle(19, 3)
rectangle2 = Rectangle(39, 4)
rectangle3 = Rectangle(8, 7)

figure_list = [square1, square2, rectangle1, rectangle2, rectangle3]

for figure in figure_list:
    figure.info()
