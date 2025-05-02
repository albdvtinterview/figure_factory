import abc
import math
from figure_factory import Figure, FigureFactory


class Circle(Figure):
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        self.radius = radius

    def get_area(self):
        return math.pi * self.radius ** 2


class Rectangle(Figure):
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive.")
        self.width = width
        self.height = height

    def get_area(self):
        return self.width * self.height


class Triangle(Figure):
    def __init__(self, a, b, c):
        if a <= 0 or b <= 0 or c <= 0 or a + b <= c or a + c <= b or b + c <= a:
            raise ValueError("Invalid triangle sides.")
        self.a, self.b, self.c = a, b, c

    def get_area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s - self.a) * (s - self.b) * (s - self.c))

    def is_right_angled(self):
        sides = sorted([self.a, self.b, self.c])
        return math.isclose(sides[0] ** 2 + sides[1] ** 2, sides[2] ** 2, rel_tol=1e-9)


# Регистрация новых типов фигур
FigureFactory.register_new_figure("circle", Circle)
FigureFactory.register_new_figure("rectangle", Rectangle)
FigureFactory.register_new_figure("triangle", Triangle)

# Создание фигур
circle = FigureFactory.create_new_figure("circle", 5)
rectangle = FigureFactory.create_new_figure("rectangle", 4, 6)
triangle = FigureFactory.create_new_figure("triangle", 3, 4, 5)

# Вывод результата
print(f"Площадь круга: {circle.get_area()}")
print(f"Площадь прямоугольника: {rectangle.get_area()}")
print(f"Площадь треугольника: {triangle.get_area()}\nТреугольник прямой? - {triangle.is_right_angled()}")
