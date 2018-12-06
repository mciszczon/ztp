class Matrix:
    """
    Handles the creation, modification and read-operations
    on a 2-dimensional array (a Matrix)
    """
    width = 0
    height = 0
    dimensions = (0, 0)
    array = list()

    def __init__(self, word1: int, word2: int) -> None:
        self.width = len(word1) + 1
        self.height = len(word2) + 1
        self.dimensions = (self.width, self.height)
        
        self.__generate_2d_array()
        self.__enum_words()

    def __generate_2d_array(self) -> None:
        """ Creates the array and fills it with 0s"""
        self.array = [[0 for x in range(self.width)] for y in range(self.height)]

    def __enum_words(self) -> None:
        """ Fills first row and first column with incremental values"""
        for i in range(self.width):
            self.array[0][i] = i
        for i in range(self.height):
            self.array[i][0] = i

    @property
    def right_bottom(self) -> int:
        """ Returns the right-bottom value from matrix"""
        return self.array[-1][-1]
