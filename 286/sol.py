# 286. Walls and Gates

class Solution(object):

    def walls(self, arr):
        self.directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        for i, row in enumerate(arr):
            for j, cell in enumerate(row):
                if cell == 0:
                    arr = self.distances_for_gate(i, j, arr, 0)


    def distances_for_gate(self, row, col, arr, distance):
        # fixup, won't work, but logic is correct
        if row < 0 or col < 0 or row >= len(arr) or col >= len(arr[0]) or arr[row][col] == -1 or distance >= arr[row][col]:
            return arr

        arr[row][col] = distance

        for direction in self.directions:
            (newrow, newcol) =  (row, col) - direction
            arr = self.distances_for_gate(newrow, newcol, arr, distance + 1)
            
        return arr