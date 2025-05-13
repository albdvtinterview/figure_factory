import inspect
from importlib import import_module
from figure import Figure
from typing import Type


class FigureFactory:
    figure_class_registry = []

    @staticmethod
    def __register_new_figure(in_cls):
        FigureFactory.figure_class_registry.append(in_cls)

    @staticmethod
    def get_all_figure_classes(module_name: str) -> list[Type[Figure]] | None:
        figure_classes = []
        try:
            module = import_module(module_name)
            for name, obj in inspect.getmembers(module):
                if inspect.isclass(obj) and issubclass(obj, Figure) and obj is not Figure:
                    figure_classes.append(obj)
        except ImportError:
            print(f"Error: Module '{module_name}' not found.")
            return None
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return None
        return figure_classes

    @staticmethod
    def create_new_figure(figure_class, *args) -> Type[Figure]:
        if isinstance(figure_class, Figure):
            raise ValueError(f"Unknown figure class: {figure_class}")

        if figure_class not in FigureFactory.figure_class_registry:
            FigureFactory.__register_new_figure(figure_class)
            return figure_class(*args)
        return figure_class(*args)
