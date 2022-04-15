"""
# @leetup=custom
# @leetup=info id=124 lang=python3 slug=binary-tree-maximum-path-sum


# A path in a binary tree is a sequence of nodes where each pair of adjacent
# nodes in the sequence has an edge connecting them. A node can only appear in the
# sequence at most once. Note that the path does not need to pass through the
# root.
#
# The path sum of a path is the sum of the node's values in the path.
#
# Given the `root` of a binary tree, return *the maximum path sum of any
# non-empty path*.
#
#
# Example 1:
#
# []
# Input: root = [1,2,3]
# Output: 6
# Explanation: The optimal path is 2 -> 1 -> 3 with a path sum of 2 + 1 + 3 =
# 6.
#
# Example 2:
#
# []
# Input: root = [-10,9,20,null,null,15,7]
# Output: 42
# Explanation: The optimal path is 15 -> 20 -> 7 with a path sum of 15 + 20 +
# 7 = 42.
#
#
# Constraints:
#
# * The number of nodes in the tree is in the range `[1, 3 * 104]`.
# * `-1000 <= Node.val <= 1000`
#
"""
# @leetup=custom
# @leetup=inject:before_code_ex
from utils import *
# @leetup=inject:before_code_ex

# @leetup=code
class Solution:
    maxsum = 0

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        """
        >>> Solution().maxPathSum(deserialize('[1,2,3]'))
        6
        >>> Solution().maxPathSum(deserialize('[-10,9,20,null,null,15,7]'))
        42
        >>> Solution().maxPathSum(deserialize('[-10,9,20,9,null,15,7]'))
        43
        >>> Solution().maxPathSum(deserialize('[-10,9,20,15,7,null,9]'))
        43
        """
        maxsum = 0
        # subtreemax = {}

        def traverse(node: TreeNode) -> int:
            if not node:
                return 0
            l = traverse(node.left)
            r = traverse(node.right)
            sum_ = node.val
            if l > 0:
                sum_ += l
            if r > 0:
                sum_ += r
            # nonlocal subtreemax
            # subtreemax[node] = sum_
            nonlocal maxsum
            maxsum = max(maxsum, sum_)
            maxleaf = max(l, r)
            if maxleaf > 0:
                return maxleaf + node.val
            else:
                return node.val
        traverse(root)
        # d(subtreemax)
        return maxsum
# @leetup=code


# @leetup=inject:after_code
if __name__ == "__main__":
    import doctest
    doctest.testmod()
# @leetup=inject:after_code
