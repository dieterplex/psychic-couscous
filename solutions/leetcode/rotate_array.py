"""
# @leetup=custom
# @leetup=info id=189 lang=python3 slug=rotate-array


# Given an array, rotate the array to the right by `k` steps, where `k` is
# non-negative.
#
#
# Example 1:
#
# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
# Example 2:
#
# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
#
# Constraints:
#
# * `1 <= nums.length <= 105`
# * `-231 <= nums[i] <= 231 - 1`
# * `0 <= k <= 105`
#
#
# Follow up:
#
# * Try to come up with as many solutions as you can. There are at least three
#   different ways to solve this problem.
# * Could you do it in-place with `O(1)` extra space?
#
"""
# @leetup=custom
# @leetup=inject:before_code_ex
from utils import *
# @leetup=inject:before_code_ex

# @leetup=code

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.

        >>> input, k = [1,2,3,4,5,6,7], 10
        >>> Solution().rotate(input, k); assert input == [5,6,7,1,2,3,4]
        >>> input, k = [-1,-100,3,99], 2
        >>> Solution().rotate(input, k); assert input == [3,99,-1,-100]
        >>> input, k = [1,2], 5
        >>> Solution().rotate(input, k); assert input == [2,1]
        """
        k %= len(nums)
        if k:
            nums[:] = nums[::-1]
            nums[:] = nums[k-1::-1] + nums[:k-1:-1]
            # nums[:k], nums[k:] = nums[-k:], nums[:-k]
# @leetup=code

def rev3(nums, k):
    def numReverse(start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1
    n = len(nums)
    k %= n
    if k:
        numReverse(0, n - 1)
        numReverse(0, k - 1)
        numReverse(k, n - 1)

def pysublist(nums, k):
    k %= len(nums)
    nums[:] = nums[-k:]+nums[:-k]

def hardway(nums: List[int], k: int):
    def gcd(a, b) -> int:
        if b == 0:
            return a
        return gcd(b, a % b)

    n = len(nums)
    if n == 1:
        return
    if k > n:
        k %= n
    k = n - k
    if k in (0, n):
        return
    shift_gcd = gcd(k, n)
    for i in range(shift_gcd):
        temp = nums[i]
        j = i
        while 1:
            next_ = j + k
            # d(f"nums: {nums}, i: {i}, j: {j}, next_: {next_}")
            if next_ >= n:
                next_ -= n
            if next_ == i:
                break
            nums[j] = nums[next_]
            j = next_
        nums[j] = temp
        # d(f"nums: {nums}, i: {i}, j: {j}, next_: {next_}")
    # d(f"nums: {nums}")

# @leetup=inject:after_code
if __name__ == "__main__":
    import doctest
    doctest.testmod()
# @leetup=inject:after_code
