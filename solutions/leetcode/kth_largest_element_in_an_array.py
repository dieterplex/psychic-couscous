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
import sys


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
    nums.sort()  # sort inplace
    return nums[-k]
    # return sorted(nums)[-k]  # new list


def sol2(nums, k):
    "partitioning. faster then sol1"

    def getSmallest(nums, l, r, idx):
        d(f'getSmallest l={l}, r={r}, indexInLR={idx-1}\tnums={nums}')
        if l >= r:
            return nums[l]
        # q: partition point, new bound index
        q = partit(nums, l, r)
        # distance to left bound in range
        distance = q - l + 1
        if distance == idx:
            d(f'ans={nums[q]}\tnums={nums}\n')
            return nums[q]
        if idx < distance:
            return getSmallest(nums, l, q - 1, idx)
        else:
            return getSmallest(nums, q + 1, r, idx - distance)

    def partit(nums, l, r):
        # optimize time complex O(n) ~ O(n^2), from halfrost/leetcode-go
        p = l + random.randint(0, r - l)
        d(f'random par idx: "l={l}" <= "idx={p}" <= "r={r}"')
        d(f'swap nums[idx={p}]={nums[p]} with nums[r={r}]={nums[r]}\t{nums}')
        swap(nums, p, r)
        # let nums[l..i] <= nums[r] < nums[i+1..j-1]
        i = l - 1  # i: idx for next small num
        for j in range(l, r):
            if nums[j] <= nums[r]:
                i += 1
                if i != j:
                    d(f'swap nums[i={i}]={nums[i]} with nums[j={j}]={nums[j]}\t{nums}')
                    swap(nums, i, j)
        d(f'swap nums[i+1={i+1}]={nums[i+1]} with nums[r={r}]={nums[r]}\t{nums}')
        swap(nums, i+1, r)
        return i + 1

    def swap(nums, i, j):
        if i != j:
            nums[i], nums[j] = nums[j], nums[i]

    m = len(nums) - k + 1  # final 1-based index
    d(f"nums={nums}, k={k}, target index={m-1}")
    return getSmallest(nums, 0, len(nums) - 1, m)


def d(msg: str):
    "`export PYTHONUNBUFFERED=x` when debug"
    if os.getenv('UVA_DEBUG'):
        print(msg, file=sys.stderr)


if __name__ == '__main__':
    import doctest
    doctest.testmod()

# @leetup=code
