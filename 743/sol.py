# 743. Network Delay Time
# https://leetcode.com/problems/network-delay-time/

import sys
from heapq import *

class Solution(object):
    def network_delay_time_djikstras(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        distances = [sys.maxsize for i in range(n)]
        adj = [[] for i in range(n)]
        distances[k - 1] = 0
        q = [(0, k - 1)]
        
        for origin, dest, weight in times:
            adj[origin - 1].append((dest - 1, weight))

        while len(q):
            distance, node = heappop(q)

            for dest, weight in adj[node]: 
                if distance + weight < distances[dest]:
                    distances[dest] = distance + weight
                    heappush(q, (distances[dest], dest))
        
        time = max(distances)
        if time == sys.maxsize:
            return -1
        else:
            return time 

        # E = # of edges = len(times)   
        # space: E + n
        # time: Elog(E) 
    
    def network_delay_time_bellman_ford(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        time_to = [sys.maxsize for i in range(n)]
        time_to[k - 1] = 0
        for i in range(n-1):
            made_change = False
            for origin, dest, weight in times:
                if time_to[origin - 1] + weight < time_to[dest - 1]:
                    time_to[dest - 1] = time_to[origin - 1] + weight
                    made_change = True

            if made_change == False:
                break 

        print(time_to)
        time = max(time_to)
        if time == sys.maxsize:
            return -1
        else:
            return time 

        # E = # of edges = len(times)   
        # space: n
        # time: nE     

    def __init__(self):
        print("initialized")

    def test1(self, times, n, k):
        return self.network_delay_time_djikstras(times, n, k)

    def test2(self, times, n, k):
        return self.network_delay_time_bellman_ford(times, n, k)


times1 = [
        (1, 2, 7),
        (1, 4, 5),
        (2, 3, 8),
        (2, 4, 9),
        (2, 5, 7),
        (3, 5, 5),
        (4, 5, 15),
        (4, 6, 6),
        (5, 6, 8),
        (5, 7, 9),  
        (6, 7, 11)
    ]
s = Solution()
print(s.test2(times1, 7, 1))