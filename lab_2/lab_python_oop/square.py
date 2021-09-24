from lab_python_oop.rectangle import Rectangle


class Square(Rectangle):
    """
    Класс «Квадрат» наследуется от класса «Прямоугольник».
    """
    FIGURE_TYPE = "Квадрат"

    @classmethod
    def get_figure_type(cls): # метод для возврата типа фигуры
        return cls.FIGURE_TYPE

    def __init__(self, color_param, side_param): # конструктор класса
        """
        Класс должен содержать конструктор по параметрам «сторона» и «цвет».
        super() организует доступ к унаследованным элементам
        """
        self.side = side_param
        super().__init__(color_param, self.side, self.side)

    def __repr__(self): # метод отвечает за строковое представление объекта
        return '{} {} цвета со стороной {} площадью {}.'.format(
            Square.get_figure_type(),
            self.fc.colorproperty,
            self.side,
            self.square()
        )
