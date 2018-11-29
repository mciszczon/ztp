from .matrix import Matrix

"""
1. √ Store words separately (it's already stored as strs are iterable)
2. √ Create Matrix[len(A), len(B)]
3. √ Fill Matrix[0] with range(0, len(A)+1)
5. Iterate over rows:
    Iterate columns (Y):
        Matrix[X][Y] = Matrix[X][Y-1] + 1
                        <or> Matrix[X-1][Y] + 1 
                        <or> Matrix[X-1][Y-1] + 1
                        <or> Matrix[X-1][Y-1] + 0 if same letters
6. Matrix[len(A), len(B)] is the answer!
"""

def levenstein(word1: str, word2: str) -> int:
    width, height = len(word1) + 1, len(word2) + 1
    matrix = Matrix(width, height).matrix

    for row_i, row in enumerate(matrix):
        for col_i, col in enumerate(row):
            if col_i > 0 and row_i > 0:
                matrix[row_i][col_i] = matrix[row_i][col_i-1] + 1
    
    for row in matrix:
        print(row)

    return True