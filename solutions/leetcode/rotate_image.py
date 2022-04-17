# @leetup=custom
"""
# @leetup=info id=48 lang=python3 slug=rotate-image
# You are given an `n x n` 2D `matrix` representing an image, rotate the image by
# 90 degrees (clockwise).
#
# You have to rotate the image [in-place][1], which means you have to modify
# the input 2D matrix directly. DO NOT allocate another 2D matrix and do the
# rotation.
#
#
# Example 1:
#
# []
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
#
# Example 2:
#
# []
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#
#
# Constraints:
#
# * `n == matrix.length == matrix[i].length`
# * `1 <= n <= 20`
# * `-1000 <= matrix[i][j] <= 1000`
#
# [1] https://en.wikipedia.org/wiki/In-place_algorithm
#
"""
# @leetup=custom
# @leetup=inject:before_code_ex
from utils import List, d
# from utils.matrix import pprint as mpprint
# @leetup=inject:before_code_ex
# @leetup=code


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.

        >>> m = [[1,2,3],[4,5,6],[7,8,9]]
        >>> Solution().rotate(m)
        >>> assert m == [[7,4,1],[8,5,2],[9,6,3]]
        >>> m = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
        >>> Solution().rotate(m)
        >>> assert m == [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
        >>> import numpy as np
        >>> m = np.random.randint(-1000, 1001, size=(20, 20))
        >>> mrot = m.copy()
        >>> Solution().rotate(m)
        >>> assert np.array_equal(m, np.rot90(mrot, 3))
        """
        mirror_diag(matrix)
        # rot(matrix)


def rot(matrix):
    # d(matrix)
    temp = 0
    n = len(matrix)-1
    for i in range(len(matrix)//2):
        for j in range(i, n - i):
            temp = matrix[j][n-i]
            matrix[j][n-i] = matrix[i][j]
            matrix[i][j] = matrix[n-j][i]
            matrix[n-j][i] = matrix[n-i][n-j]
            matrix[n-i][n-j] = temp
            # d(f'n={n} i={i} j={j}')
            # d(matrix)


def mirror_diag(matrix):
    # d(matrix)
    n = len(matrix)
    n1 = n - 1
    for i in range(n):
        for j in range(n - i):
            matrix[i][j], matrix[n1 - j][n1 -
                                         i] = matrix[n1 - j][n1 - i], matrix[i][j]
    for i in range(n // 2):
        for j in range(n):
            matrix[i][j], matrix[n1 - i][j] = matrix[n1 - i][j], matrix[i][j]
    # 2nd way
    # for i in range(n // 2):
    #     for j in range(n):
    #         swap(matrix[i][j], matrix[n - 1 - i][j])
    # for i in range(n):
    #     for j in range(i + 1, n):
    #         swap(matrix[i][j], matrix[j][i])
# @leetup=code


# @leetup=inject:after_code
if __name__ == "__main__":
    import doctest
    doctest.testmod()
# @leetup=inject:after_code
