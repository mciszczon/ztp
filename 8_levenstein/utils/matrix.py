class Matrix:
    width = 0
    height = 0
    dimensions = (0, 0)
    matrix = list()

    def __init__(self, width: int, height: int) -> None:
        self.width = width
        self.height = height
        self.dimensions = (width, height)
        self.matrix = [[0 for x in range(width)] for y in range(height)]
        self.__initialize()

    def __initialize(self) -> None:
        for i in range(self.width):
            self.matrix[0][i] = i
        for i in range(self.height):
            self.matrix[i][0] = i