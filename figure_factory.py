import abc


class Figure(abc.ABC):
    @abc.abstractmethod
    def get_area(self):
        pass


class FigureFactory:
    figure_names = {}

    @staticmethod
    def register_new_figure(figure_name, cls):
        if not issubclass(cls, Figure):
            raise TypeError(f"Specified class '{cls}' must be a subclass of the Figure parent.")
        if figure_name in FigureFactory.figure_names:
            raise ValueError(f"Figure type '{figure_name}' is already registered.")
        FigureFactory.figure_names[figure_name] = cls

    @staticmethod
    def create_new_figure(figure_name, *args):
        cls = FigureFactory.figure_names.get(figure_name)
        if cls is None:
            raise ValueError(f"Unknown figure class: {cls}")
        return cls(*args)
    