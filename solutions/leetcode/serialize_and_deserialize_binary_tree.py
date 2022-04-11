# @leetup=custom
# @leetup=info id=297 lang=python3 slug=serialize-and-deserialize-binary-tree


# Serialization is the process of converting a data structure or object into a
# sequence of bits so that it can be stored in a file or memory buffer, or
# transmitted across a network connection link to be reconstructed later in the
# same or another computer environment.
# Design an algorithm to serialize and deserialize a binary tree. There is no
# restriction on how your serialization/deserialization algorithm should work. You
# just need to ensure that a binary tree can be serialized to a string and this
# string can be deserialized to the original tree structure.
# Clarification: The input/output format is the same as [how LeetCode
# serializes a binary tree][1]. You do not necessarily need to follow this format,
# so please be creative and come up with different approaches yourself.
# Example 1:
# []
# Input: root = [1,2,3,null,null,4,5]
# Output: [1,2,3,null,null,4,5]
# Example 2:
# Input: root = []
# Output: []
# Constraints:
# * The number of nodes in the tree is in the range `[0, 104]`.
# * `-1000 <= Node.val <= 1000`
# [1] https://support.leetcode.com/hc/en-us/articles/360011883654-What-does-1-null-2-3-mean-in-binary-tree-representation-

# @leetup=custom
# @leetup=code

import collections
import io
import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x, left=None, right=None):
        self.val = x
        self.left = left
        self.right = right

    def __repr__(self):
        # return Codec().serialize(self)
        if self.left and self.right:
            leaf = f', {self.left}, {self.right}'
        elif self.left:
            leaf = f', left={self.left}'
        elif self.right:
            leaf = f', right={self.right}'
        else:
            leaf = ""
        return f'TreeNode({self.val}{leaf})'


class Codec:
    """de/serializing for binary tree"""

    def serialize(self, root):
        """Encodes a tree to a single string.

        >>> Codec().serialize(testdata1())
        '[1,2,3,null,null,4,5]'
        >>> Codec().serialize(testdata2())
        '[5,4,7,3,null,2,null,-1,null,9]'

        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return '[]'
        pos = 0
        out = io.StringIO()
        out.write("[")
        q = collections.deque([root])
        while q:
            node = q.pop()
            if isinstance(node, str):
                out.write(node)
            else:
                val = str(node.val)
                for leaf in (node.left, node.right):
                    if leaf is None:
                        q.appendleft('null')
                    if isinstance(leaf, TreeNode):
                        q.appendleft(leaf)
                out.write(val)
                pos = out.tell()
            if q:
                out.write(',')
        out.truncate(pos)
        outdata = out.getvalue() + ']'
        # print(outdata, file=sys.stderr)
        return outdata

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        >>> Codec().deserialize('[1,2,3,null,null,4,5]')
        TreeNode(1, TreeNode(2), TreeNode(3, TreeNode(4), TreeNode(5)))
        >>> Codec().deserialize('[]')

        :type data: str
        :rtype: TreeNode
        """
        if data == '[]':
            return None
        nodes = [None if val == 'null' else TreeNode(int(val))
                 for val in data.strip('[]{}').split(',')]
        kids = nodes[::-1]
        root = kids.pop()
        for node in nodes:
            if node:
                if kids:
                    node.left = kids.pop()
                if kids:
                    node.right = kids.pop()
        return root


def drawtree(root):
    """https://leetcode.com/problems/recover-binary-search-tree/discuss/32539/Tree-Deserializer-and-Visualizer-for-Python"""
    def height(root):
        return 1 + max(height(root.left), height(root.right)) if root else -1

    def jumpto(x, y):
        t.penup()
        t.goto(x, y)
        t.pendown()

    def draw(node, x, y, dx):
        if node:
            t.goto(x, y)
            jumpto(x, y-20)
            t.write(node.val, align='center', font=('Arial', 12, 'normal'))
            draw(node.left, x-dx, y-60, dx/2)
            jumpto(x, y-20)
            draw(node.right, x+dx, y-60, dx/2)
    import turtle
    t = turtle.Turtle()
    t.speed(0)
    turtle.delay(0)
    h = height(root)
    jumpto(0, 30*h)
    draw(root, 0, 30*h, 40*h)
    t.hideturtle()
    turtle.mainloop()


def testdata1():
    # [1,2,3,None,None,4,5]
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)
    return root


def testdata2():
    # [5,4,7,3,null,2,null,-1,null,9]
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.left = TreeNode(3)
    root.left.left.left = TreeNode(-1)
    root.right = TreeNode(7)
    root.right.left = TreeNode(2)
    root.right.left.left = TreeNode(9)
    return root


if __name__ == '__main__':
    import doctest
    doctest.testmod()

    ser = Codec()
    deser = Codec()
    ans = testdata1()
    assert str(deser.deserialize(ser.serialize(ans))) == str(ans)
    assert ser.serialize(deser.deserialize(
        '[1,2,3,null,null,4,5]')) == '[1,2,3,null,null,4,5]'
    assert deser.deserialize(ser.serialize([])) == None

    # drawtree(deser.deserialize(
    #     '[2,1,3,0,7,9,1,2,null,1,0,null,null,8,8,null,null,null,null,7]'))

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
# @leetup=code
