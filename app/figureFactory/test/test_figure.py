import unittest
from typing import List, Type
from app.figureFactory.src.figure_factory import FigureFactory
from app.figureFactory.src.figure import Figure
from math import pi
from app.figureFactory.src.figures import Circle, Rectangle, Triangle


class TestFigureFactory(unittest.TestCase):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.figure_manager = None

    def setUp(self):
        self.figure_manager = FigureFactory()

    def test_figure_manager_obj(self):
        self.assertIsNotNone(self.figure_manager)

    def test_get_all_figure_classes_func(self):
        clss = self.figure_manager.get_all_figure_classes("figures")
        self.assertIsInstance(clss, List)
        for cls in self.figure_manager.get_all_figure_classes("figures"):
            self.assertTrue(issubclass(cls, Figure))

    def test_circle(self):
        circle_class = Type[Figure]
        clss = self.figure_manager.get_all_figure_classes("figures")
        for cls in clss:
            if cls.__name__ == "Circle":
                circle_class = cls

        # test circle __init_() with figure_manager
        with self.assertRaises(ValueError):
            self.figure_manager.create_new_figure(circle_class, -5)
        with self.assertRaises(ValueError):
            self.figure_manager.create_new_figure(circle_class, 0)
        with self.assertRaises(TypeError):
            self.figure_manager.create_new_figure(circle_class, "five")
        # test circle get_area() with figure_manager
        self.assertAlmostEqual(self.figure_manager.create_new_figure(circle_class, 5).get_area(), pi * 25, places=7)

        # test circle __init__() using imported class
        self.assertRaises(ValueError, Circle, -5.0)
        self.assertRaises(ValueError, Circle, 0.0)
        self.assertRaises(TypeError, Circle, "five")
        # test circle get_area() using imported class
        self.assertAlmostEqual(Circle(5.0).get_area(), pi * 25, places=7)

    def test_rectangle(self):
        rectangle_class = Type[Figure]
        clss = self.figure_manager.get_all_figure_classes("figures")
        for cls in clss:
            if cls.__name__ == "Rectangle":
                rectangle_class = cls

        # test rectangle __init_() with figure_manager
        with self.assertRaises(ValueError):
            self.figure_manager.create_new_figure(rectangle_class, -4.0, 6.0)
        with self.assertRaises(ValueError):
            self.figure_manager.create_new_figure(rectangle_class, 4.0, -6.0)
        with self.assertRaises(ValueError):
            self.figure_manager.create_new_figure(rectangle_class, 0.0, 6.0)
        with self.assertRaises(ValueError):
            self.figure_manager.create_new_figure(rectangle_class, 4.0, 0.0)
        with self.assertRaises(TypeError):
            self.figure_manager.create_new_figure(rectangle_class, "four", 0.0)
        with self.assertRaises(TypeError):
            self.figure_manager.create_new_figure(rectangle_class, 4.0, "six")
        with self.assertRaises(TypeError):
            self.figure_manager.create_new_figure(rectangle_class, "four", "six")
        # test rectangle get_area() with figure_manager
        self.assertEqual(self.figure_manager.create_new_figure(rectangle_class, 4.0, 6.0).get_area(), 24.0)

        # test rectangle __init__() using imported class
        self.assertRaises(ValueError, Rectangle, -4.0, 6.0)
        self.assertRaises(ValueError, Rectangle, 4.0, -6.0)
        self.assertRaises(ValueError, Rectangle, 0.0, 6.0)
        self.assertRaises(ValueError, Rectangle, 4.0, 0.0)
        self.assertRaises(TypeError, Rectangle, "four", 6.0)
        self.assertRaises(TypeError, Rectangle, 4.0, "six")
        self.assertRaises(TypeError, Rectangle, "four", "six")
        # test rectangle get_area() using imported class
        self.assertEqual(Rectangle(4.0, 6.0).get_area(), 24.0)

    def test_triangle(self):
        triangle_class = Type[Figure]
        clss = self.figure_manager.get_all_figure_classes("figures")
        for cls in clss:
            if cls.__name__ == "Triangle":
                triangle_class = cls

        # test triangle __init_() with figure_manager
        with self.assertRaises(ValueError):
            self.figure_manager.create_new_figure(triangle_class, 1.0, 1.0, 3.0)
        with self.assertRaises(ValueError):
            self.figure_manager.create_new_figure(triangle_class, -3.0, 4.0, 5.0)
        with self.assertRaises(ValueError):
            self.figure_manager.create_new_figure(triangle_class, 3.0, 4.0, 0.0)
        with self.assertRaises(ValueError):
            self.figure_manager.create_new_figure(triangle_class, 3.0, 0.0, 4.0)
        with self.assertRaises(ValueError):
            self.figure_manager.create_new_figure(triangle_class, 0.0, 3.0, 4.0)
        with self.assertRaises(TypeError):
            self.figure_manager.create_new_figure(triangle_class, "first", 3.0, 4.0)
        with self.assertRaises(TypeError):
            self.figure_manager.create_new_figure(triangle_class, 3.0, "second", 4.0)
        with self.assertRaises(TypeError):
            self.figure_manager.create_new_figure(triangle_class, 4.0, 3.0, "third")
        with self.assertRaises(TypeError):
            self.figure_manager.create_new_figure(triangle_class, "third", "second", "third")
        # test rectangle get_area() with figure_manager
        tr_1 = self.figure_manager.create_new_figure(triangle_class, 3.0, 4.0, 5.0)
        self.assertEqual(tr_1.get_area(), 6.0)
        self.assertTrue(tr_1.is_right_angled())

        # test triangle __init__() using imported class
        self.assertRaises(ValueError, Triangle, 1.0, 1.0, 3.0)
        self.assertRaises(ValueError, Triangle, -3.0, 4.0, 5.0)
        self.assertRaises(ValueError, Triangle, 3.0, 4.0, 0.0)
        self.assertRaises(ValueError, Triangle, 3.0, 0.0, 4.0)
        self.assertRaises(ValueError, Triangle, 0.0, 3.0, 4.0)
        self.assertRaises(TypeError, Triangle, "first", 3.0, 4.0)
        self.assertRaises(TypeError, Triangle, 3.0, "second", 4.0)
        self.assertRaises(TypeError, Triangle, 4.0, 3.0, "third")
        self.assertRaises(TypeError, Triangle, "first", "second", "third")
        # test triangle get_area() using imported class
        tr_2 = Triangle(3.0, 4.0, 5.0)
        self.assertEqual(tr_2.get_area(), 6.0)
        self.assertTrue(tr_2.is_right_angled())


if __name__ == '__main__':
    unittest.main()

