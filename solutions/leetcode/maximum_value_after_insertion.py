"""
# @leetup=custom
# @leetup=info id=1881 lang=python3 slug=maximum-value-after-insertion


# You are given a very large integer `n`, represented as a string,​​​​​​ and an integer
# digit `x`. The digits in `n` and the digit `x` are in the inclusive range
# `[1, 9]`, and `n` may represent a negative number.
#
# You want to maximize `n`'s numerical value by inserting `x` anywhere in
# the decimal representation of `n`​​​​​​. You cannot insert `x` to the left of the
# negative sign.
#
# * For example, if `n = 73` and `x = 6`, it would be best to insert it between
#   `7` and `3`, making `n = 763`.
# * If `n = -55` and `x = 2`, it would be best to insert it before the first `5`,
#   making `n = -255`.
#
# Return *a string representing the maximum value of *`n`*​​​​​​ after the
# insertion*.
#
#
# Example 1:
#
# Input: n = "99", x = 9
# Output: "999"
# Explanation: The result is the same regardless of where you insert 9.
#
# Example 2:
#
# Input: n = "-13", x = 2
# Output: "-123"
# Explanation: You can make n one of {-213, -123, -132}, and the largest of th
# ose three is -123.
#
#
# Constraints:
#
# * `1 <= n.length <= 10^5`
# * `1 <= x <= 9`
# * The digits in `n`​​​ are in the range `[1, 9]`.
# * `n` is a valid representation of an integer.
# * In the case of a negative `n`,​​​​​​ it will begin with `'-'`.
#
"""

# @leetup=custom
# @leetup=code
from utils import check

class Solution:
    def maxValue(self, n: str, x: int) -> str:
        """
        >>> assert Solution().maxValue("99", 9) == "999", "wrong answer"
        >>> assert Solution().maxValue("-13", 2) == "-123", "wrong answer"
        >>> assert Solution().maxValue("13", 2) == "213", "wrong answer"
        >>> assert Solution().maxValue("73", 6) == "763", "wrong answer"
        >>> assert Solution().maxValue("-132", 3) == "-1323", "wrong answer"
        """
        digit = str(x)
        neg = n[0] == '-'
        idx = 1 if neg else 0
        while idx < len(n):
            if (digit > n[idx]) and not neg:
                break
            if (digit < n[idx]) and neg:
                break
            idx += 1
        return check(n[:idx] + digit + n[idx:])
        # @lee215
        # for i in range(len(n)):
        #     if [digit > n[i], digit < n[i]][neg]:
        #         return n[:i] + digit + n[i:]
        # return n + digit


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# @leetup=code
