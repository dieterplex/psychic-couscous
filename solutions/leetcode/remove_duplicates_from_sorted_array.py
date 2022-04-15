"""
# @leetup=custom
# @leetup=info id=26 lang=python3 slug=remove-duplicates-from-sorted-array


# Given an integer array `nums` sorted in non-decreasing order, remove the
# duplicates [in-place][1] such that each unique element appears only
# once. The relative order of the elements should be kept the same.
#
# Since it is impossible to change the length of the array in some languages, you
# must instead have the result be placed in the first part of the array
# `nums`. More formally, if there are `k` elements after removing the duplicates,
# then the first `k` elements of `nums` should hold the final result. It does not
# matter what you leave beyond the first `k` elements.
#
# Return `k`* after placing the final result in the first *`k`* slots of *`nums`.
#
# Do not allocate extra space for another array. You must do this by
# modifying the input array [in-place][2] with O(1) extra memory.
#
# Custom Judge:
#
# The judge will test your solution with the following code:
#
# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length
# int k = removeDuplicates(nums); // Calls your implementation
# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
#
# If all assertions pass, then your solution will be accepted.
#
#
# Example 1:
#
# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements 
# of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are undersco
# res).
#
# Example 2:
#
# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements
#  of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are undersco
# res).
#
#
# Constraints:
#
# * `1 <= nums.length <= 3 * 104`
# * `-100 <= nums[i] <= 100`
# * `nums` is sorted in non-decreasing order.
#
# [1] https://en.wikipedia.org/wiki/In-place_algorithm
# [2] https://en.wikipedia.org/wiki/In-place_algorithm
#
"""
# @leetup=custom
# @leetup=inject:before_code_ex
from utils import *
# @leetup=inject:before_code_ex

# @leetup=code
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        >>> nums = [1,1,2]
        >>> Solution().removeDuplicates(nums)
        2
        >>> assert nums[0: 2] == [1,2]
        >>> nums = [0,0,1,1,1,2,2,3,3,4]
        >>> Solution().removeDuplicates(nums)
        5
        >>> assert nums[0: 5] == [0,1,2,3,4]
        """
        slot2rep = 1
        for i, el in enumerate(nums):
            if i > 0 and el > nums[i-1]:
                # not dupe, replace and slot2rep++
                nums[slot2rep] = el
                slot2rep += 1
            # d(f'{i}, {nums}')
        return slot2rep
# @leetup=code


# @leetup=inject:after_code
if __name__ == "__main__":
    import doctest
    doctest.testmod()
# @leetup=inject:after_code
