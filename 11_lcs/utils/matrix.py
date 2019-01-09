from logging import getLogger
logger = getLogger(__name__)


class Matrix:
    """
    Handles the creation, modification and read-operations
    on a 2-dimensional array (a Matrix)
    """
    string1 = ""
    string2 = ""
    width = 0
    height = 0
    dimensions = (0, 0)
    array = list()

    def __init__(self, string1: int, string2: int) -> None:
        self.string1 = string1
        self.string2 = string2
        self.width = len(string1)
        self.height = len(string2)
        self.dimensions = (self.width, self.height)

        self._generate_2d_array()
        self._calculate()

    def _generate_2d_array(self) -> None:
        """ Creates the array and fills it with 0s """
        self.array = [[0 for x in range(self.height+1)] for y in range(self.width+1)]

    def _calculate(self) -> None:
        """ Fill the matrix with values """
        for x in range(1, self.width+1):
            for y in range(1, self.height+1):
                if self.string1[x-1] == self.string2[y-1]:
                    self.array[x][y] = self.array[x-1][y-1] + 1
                else:
                    self.array[x][y] = max(self.array[x-1][y], self.array[x][y-1])

    @property
    def right_bottom(self) -> int:
        """ Returns the right-bottom value from matrix """
        return self.array[-1][-1]

    @property
    def lcs(self) -> float:
        """ Returns LCS from formula: 1 - [ |f(a, b)| / max(|a|, |b|) ] """
        return 1 - (self.right_bottom / max(self.width, self.height))
