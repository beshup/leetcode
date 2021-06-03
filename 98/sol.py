# 98. Validate Binary Search Tree
# https://leetcode.com/problems/validate-binary-search-tree/


class Node(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.valid(root, float('-inf'), float('inf'))
        

    def valid(self, node, lo, hi):
        if node.val <= lo or node.val >= hi:
            return False

        if node.left != None:
            if not self.valid(node.left, lo, node.val):
                return False

        if node.right != None:
            if not self.valid(node.right, node.val, hi):
                return False

        return True