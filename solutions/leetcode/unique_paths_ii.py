# @leetup=custom
# @leetup=info id=63 lang=python3 slug=unique-paths-ii


# You are given an `m x n` integer array `grid`. There is a robot initially
# located at the top-left corner (i.e., `grid[0][0]`). The robot tries to move to
# the bottom-right corner (i.e., `grid[m-1][n-1]`). The robot can only move
# either down or right at any point in time.
#
# An obstacle and space are marked as `1` or `0` respectively in `grid`. A path
# that the robot takes cannot include any square that is an obstacle.
#
# Return *the number of possible unique paths that the robot can take to reach the
# bottom-right corner*.
#
# The testcases are generated so that the answer will be less than or equal to `2
# * 109`.
#
#
# Example 1:
#
# []
# Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
# Output: 2
# Explanation: There is one obstacle in the middle of the 3x3 grid above.
# There are two ways to reach the bottom-right corner:
# 1. Right -> Right -> Down -> Down
# 2. Down -> Down -> Right -> Right
#
# Example 2:
#
# []
# Input: obstacleGrid = [[0,1],[0,0]]
# Output: 1
#
#
# Constraints:
#
# * `m == obstacleGrid.length`
# * `n == obstacleGrid[i].length`
# * `1 <= m, n <= 100`
# * `obstacleGrid[i][j]` is `0` or `1`.
#

# @leetup=custom

# @leetup=inject:before_code
from utils import *
# @leetup=inject:before_code

# @leetup=code


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        """
        >>> Solution().uniquePathsWithObstacles([[0,0,0],[0,1,0],[0,0,0]])
        2
        >>> Solution().uniquePathsWithObstacles([[0,1],[0,0]])
        1
        >>> Solution().uniquePathsWithObstacles([[0]])
        1
        >>> Solution().uniquePathsWithObstacles([[1,0]])
        0
        >>> Solution().uniquePathsWithObstacles([[0,0,0,0,0,1,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,1,0,0,0,0,1,0,1,0,1,0,0],[1,0,0,0,0,0,1,0,0,0,0,0,1,0,1,1,0,1],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,0,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,0,1,0],[0,0,0,0,0,1,0,0,0,0,1,1,0,1,0,0,0,0],[1,0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,1,0],[0,0,0,0,1,0,0,0,1,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,1,0,0,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[1,1,0,0,0,0,0,0,0,0,1,0,0,0,0,1,0,0],[0,0,1,0,1,0,0,0,0,0,0,1,0,0,0,0,0,0],[0,1,0,0,0,1,0,0,0,0,0,0,0,0,1,0,0,0],[0,0,1,0,0,0,0,1,0,0,0,0,0,1,0,0,0,1],[0,1,0,1,0,1,0,0,0,0,0,0,0,1,0,0,0,0],[0,0,0,0,0,0,0,0,0,0,0,0,1,0,0,0,0,1],[1,0,1,1,0,0,0,0,0,0,1,0,1,0,0,0,1,0],[0,0,0,1,0,0,0,0,1,1,1,0,0,1,0,1,1,0],[0,1,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0],[0,1,1,0,0,1,0,0,0,0,0,0,0,1,1,0,0,0],[0,0,0,0,0,0,1,0,1,0,0,1,0,1,1,1,0,0],[0,0,0,1,0,0,0,0,0,0,0,0,0,0,1,0,1,1],[0,1,0,0,0,0,0,0,0,0,1,0,1,0,1,0,1,0],[1,0,0,1,0,1,0,0,1,0,0,0,0,0,0,0,0,0],[0,0,0,1,0,0,1,0,0,0,0,0,0,0,0,0,0,0],[0,1,0,0,0,0,0,1,0,0,0,0,0,0,1,1,1,0],[1,0,1,0,1,0,0,0,0,0,0,1,1,0,0,0,0,1],[1,0,0,0,0,0,1,1,0,0,0,1,0,0,0,0,0,0]])
        13594824
        """
        return dp_sol(obstacleGrid)


def dp_sol(g: List[List[int]]) -> int:
    """Time O(n^2), Space O(n)"""
    ylen: int = len(g[0])
    # obstacle at begin or end
    if g[0][0] or g[len(g)-1][ylen-1]:
        return 0
    count: List[int] = [0] * ylen
    count[0] = 1
    for gi in g:
        # not count for subrect that blocked at grid[i][j]
        count[0] = 1 if count[0] and not gi[0] else 0
        for j in range(1, ylen):
            if gi[j]:
                count[j] = 0
            else:
                count[j] += count[j-1]
    return count[-1]


def dfs_sol(g: List[List[int]]) -> int:
    if g[0][0] or g[-1][-1]:
        return 0
    xlen, ylen = len(g), len(g[0])
    count = [[0] * ylen] * xlen
    count[0][0] = 1

    def dfs(x, y):
        if x < 0 or y < 0 or g[x][y]:
            return 0
        if not x and not y:
            return count[0][0]
        if not count[x][y]:
            count[x][y] = dfs(x-1, y) + dfs(x, y-1)
        return count[x][y]
    return dfs(xlen-1, ylen-1)
# @leetup=code


def WilmerKrisp_sol(g: List[List[int]]) -> int:
    ymax, xmax = len(g) - 1, len(g[0]) - 1
    if g[xmax][ymax]:
        return 0  # for case when finish is obstacle
    grid = {(y, x): 1 - val for y, row in enumerate(g)
                            for x, val in enumerate(row)}

    import functools
    @functools.cache
    def fn(y, x):
        if (y, x) == (ymax, xmax):
            return 1
        return grid.get((y, x), 0) and fn(y + 1, x) + fn(y, x + 1)
    return fn(0, 0)


# @leetup=inject:after_code
if __name__ == "__main__":
    import doctest
    doctest.testmod()
# @leetup=inject:after_code
