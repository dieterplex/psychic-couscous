
"""
class:
ListNode(val=0, next=None)
method:
None     <- printList(head: ListNode, style=[None, 1], limit=100)
ListNode <- fromArray(a: list)

Author: Gongzq5/leetcode-helper
"""
from io import StringIO

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    
    def __repr__(self):
        return "<ListNode {}>".format(self.val)
    

def toStr(head, style=None, limit=100):
    """
    if style is anything but None, then output using arrow style.
    """
    curr = head
    c = 0
    s = StringIO()
    print('[', end='', file=s)
    while curr and c < limit:
        if not curr.next:
            delimiter = ""
        elif style:
            delimiter = " -> "
        else:
            delimiter = ","
        print(curr.val, end=delimiter, file=s)
        curr = curr.next
        c += 1
    print(']', end='', file=s)
    return s.getvalue()


def fromArray(a):
    """
    Return the head, construct a linkedlist from an array
    """
    dummy = ListNode(0, None)
    curr = dummy
    for e in a:
        curr.next = ListNode(e)
        curr = curr.next
    return dummy.next