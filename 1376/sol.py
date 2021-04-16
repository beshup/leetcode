# 1376. Time Needed to Inform All Employees
# https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution(object):
    def numOfMinutes(self, n, headID, manager, informTime):
        """
        :type n: int
        :type headID: int
        :type manager: List[int]
        :type informTime: List[int]
        :rtype: int
        """
        adjList = list(map(self.empty_array, manager))
        for index, m in enumerate(manager):
            if m == -1:
                continue
            adjList[m].append(index)    
            
        return self.dfs(headID, adjList, informTime)    
        
    def empty_array(self, x):
        return []
    
    def dfs(self, currentId, adjList, informTime):
        if len(adjList[currentId]) == 0:
            return 0
        
        maxMin = 0
        for subordinate in adjList[currentId]:
            maxMin = max(maxMin, self.dfs(subordinate, adjList, informTime))
        
        return maxMin + informTime[currentId]

# time: O(n)
# space: O(n)
