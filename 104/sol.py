# 104. Maximum Depth of Binary Tree
# https://leetcode.com/problems/maximum-depth-of-binary-tree/


class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def maxDepth(self, root, depth = 0):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None: return depth - 1
        return max(self.maxDepth(root.left, depth + 1), self.maxDepth(root.right, depth + 1))