"""
# @leetup=custom
# @leetup=info id=215 lang=python3 slug=kth-largest-element-in-an-array


# Given an integer array `nums` and an integer `k`, return *the* `kth` *largest
# element in the array*.
#
# Note that it is the `kth` largest element in the sorted order, not the `kth`
# distinct element.
#
#
# Example 1:
#
# Input: nums = [3,2,1,5,6,4], k = 2
# Output: 5
#
# Example 2:
#
# Input: nums = [3,2,3,1,2,4,5,5,6], k = 4
# Output: 4
#
#
# Constraints:
#
# * `1 <= k <= nums.length <= 104`
# * `-104 <= nums[i] <= 104`
#
"""

# @leetup=custom
# @leetup=code
from typing import List
import random


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        >>> Solution().findKthLargest([3,2,1,5,6,4], 2)
        5
        >>> Solution().findKthLargest([3,2,3,1,2,4,5,5,6], 4)
        4
        """
        return sol2(nums, k)


def sol1(nums, k):
    "plain sorting"
    # return sorted(nums)[-k]  # new list
    nums.sort()  # inplace
    return nums[-k]


def sol2(nums, k):
    "partitioning. faster then sol1"

    def getSmallest(nums, l, r, i):
        if l >= r:
            return nums[l]
        q = partit(nums, l, r)
        k = q - l + 1
        if k == i:
            return nums[q]
        if i < k:
            return getSmallest(nums, l, q - 1, i)
        else:
            return getSmallest(nums, q + 1, r, i - k)

    def partit(nums, l, r):
        # optimize time complex O(n)~O(n^2), see halfrost/leetcode-go
        k = l + random.randint(0, r - l)
        print(f'k={k}', file=sys.stderr)
        nums[k], nums[r] = nums[r], nums[k]
        # nums[l..i] <= nums[r] < nums[i+1..j-1]
        i = l - 1
        for j in range(l, r):
            if nums[j] <= nums[r]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
        nums[i+1], nums[r] = nums[r], nums[i+1]
        return i + 1

    m = len(nums) - k + 1  # final index
    return getSmallest(nums, 0, len(nums) - 1, m)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# @leetup=code
