# @leetup=custom
# @leetup=info id=876 lang=python3 slug=middle-of-the-linked-list


# Given the `head` of a singly linked list, return *the middle node of the linked
# list*.
#
# If there are two middle nodes, return the second middle node.
#
#
# Example 1:
#
# []
# Input: head = [1,2,3,4,5]
# Output: [3,4,5]
# Explanation: The middle node of the list is node 3.
#
# Example 2:
#
# []
# Input: head = [1,2,3,4,5,6]
# Output: [4,5,6]
# Explanation: Since the list has two middle nodes with values 3 and 4, we ret
# urn the second one.
#
#
# Constraints:
#
# * The number of nodes in the list is in the range `[1, 100]`.
# * `1 <= Node.val <= 100`
#

# @leetup=custom
from utils import *
# @leetup=code

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count = 0
        node = head
        while node:
            count += 1
            node = node.next
        count //= 2
        node = head
        while count:
            node = node.next
            count -= 1
        return node

# @leetup=code
