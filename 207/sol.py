# 207. Course Schedule
# https://leetcode.com/problems/course-schedule/

class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        adjList = []
        inDegrees = [0] * numCourses
        for i in range(numCourses):
            adjList.append([])

        for pair in prerequisites:
            adjList[pair[1]].append(pair[0])
            inDegrees[pair[0]] += 1 
            
        print(inDegrees)    
        print(adjList)

        return self.remove(inDegrees, adjList)

    def remove(self, inDegrees, adjList):
        zero_in_there = False
        all_removed = True
        for index, inDegree in enumerate(inDegrees):
            if inDegree != -1:
                all_removed = False
            if inDegree == 0:
                zero_in_there = True 
                inDegrees[index] = -1
                for pointingTo in adjList[index]:
                    inDegrees[pointingTo] -= 1 
                return self.remove(inDegrees, adjList)    

        if all_removed == False:
            return zero_in_there             
        
        return True
        