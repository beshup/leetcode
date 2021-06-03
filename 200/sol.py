# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/

class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """

        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        num = 1
        for i, row in enumerate(grid):
            for j, cell in enumerate(row):
                if cell == '1':
                    num += 1
                    grid = self.traverseIsland(grid, i, j, num)
                    print(grid)

        return num - 1
    
    def traverseIsland(self, grid, row, col, num):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return grid
        
        if grid[row][col] != '1':
            return grid 
        
        grid[row][col] = str(num)

        for x, y in self.directions:
            r, c = (row + x, col + y) 
            grid = self.traverseIsland(grid, r, c, num)
        
        return grid

test = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
s = Solution()
print(s.numIslands(test))