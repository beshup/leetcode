# 22. Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        self.arr = []
        self.helper(n, n, "")
        return self.arr
        
    def helper(self, o, c, s):
        if o == 0 and c == 0:
            self.arr.append(s)
            return 
        
        if o > 0:
            self.helper(o - 1, c, s + '(')
            
        if o < c and c > 0:
            self.helper(o, c - 1, s + ')')