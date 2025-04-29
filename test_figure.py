import unittest
from figure_factory import FigureFactory
import math


class TestFigureFactory(unittest.TestCase):
    def test_unknown_figure(self):
        with self.assertRaises(ValueError):
            FigureFactory.create_new_figure("some figure name")

    def test_circle(self):
        circle = FigureFactory.create_new_figure("circle", 5)
        self.assertAlmostEqual(circle.get_area(), math.pi * 25, places=7)
        with self.assertRaises(ValueError):
            FigureFactory.create_new_figure("circle", -5)
        with self.assertRaises(ValueError):
            FigureFactory.create_new_figure("circle", 0)

    def test_rectangle(self):
        rectangle = FigureFactory.create_new_figure("rectangle", 4, 6)
        self.assertEqual(rectangle.get_area(), 24)
        with self.assertRaises(ValueError):
            FigureFactory.create_new_figure("rectangle", -4, 6)
        with self.assertRaises(ValueError):
            FigureFactory.create_new_figure("rectangle", 4, -6)
        with self.assertRaises(ValueError):
            FigureFactory.create_new_figure("rectangle", 0, 6)
        with self.assertRaises(ValueError):
            FigureFactory.create_new_figure("rectangle", 4, 0)

    def test_triangle(self):
        triangle = FigureFactory.create_new_figure("triangle", 3, 4, 5)
        self.assertEqual(triangle.get_area(), 6)
        self.assertTrue(triangle.is_right_angled())

        with self.assertRaises(ValueError):
            FigureFactory.create_new_figure("triangle", 1, 1, 3)
        with self.assertRaises(ValueError):
            FigureFactory.create_new_figure("triangle", -3, 4, 5)
        with self.assertRaises(ValueError):
            FigureFactory.create_new_figure("triangle", 3, 4, 0)
        with self.assertRaises(ValueError):
            FigureFactory.create_new_figure("triangle", 3, 0, 4)
        with self.assertRaises(ValueError):
            FigureFactory.create_new_figure("triangle", 0, 3, 4)


if __name__ == '__main__':
    unittest.main()

