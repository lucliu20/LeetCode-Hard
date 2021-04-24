# https://leetcode.com/problems/critical-connections-in-a-network/

"""
Example 1:
Input: n = 4, connections = [[0,1],[1,2],[2,0],[1,3]]
Output: [[1,3]]
Explanation: [[3,1]] is also accepted.
"""

# n, connections = 4, [[0,1],[1,2],[2,0],[1,3]] # Expected: [[1,3]]
# n, connections = 4, [[0,1],[1,2],[2,0],[1,3],[3,0]] # Expected: [[]]
# n, connections = 2, [[0,1]] # Expected: [[0,1]]
# n, connections = 5, [[0,1],[1,2],[2,0],[1,3],[3,4]] # Expected: [[1,3],[3,4]]
# Test case #11:
n, connections = 6, [[0,1],[1,2],[2,0],[1,3],[3,4],[4,5],[5,3]] # Expected: [[1,3]]


# April/24/2021: Tried with Hash Table, return wrong answer on test case #11.
# The hint shows the Tarjan's algorithm.
# To be continued ...
from typing import List
import collections
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        res = []
        interConnections = collections.defaultdict(set)
        for i in range(len(connections)):
            interConnections[connections[i][0]].add(connections[i][1])
            interConnections[connections[i][1]].add(connections[i][0])
        sortedInter = dict(sorted(interConnections.items(), key = lambda x: len(x[1])))
        # test = [set() for _ in range(n)]
        # for i in range(len(connections)):
        #     test[connections[i][0]].add(connections[i][1])
        #     test[connections[i][1]].add(connections[i][0])
        for key, val in sortedInter.items():
            if len(val) == 1:
                tmp_key = val.pop()
                res.append([key, tmp_key])
                while len(sortedInter[tmp_key]) >= 1:
                    sortedInter[tmp_key].remove(key)
                    if len(sortedInter[tmp_key]) == 1:
                        key = tmp_key
                        tmp_key = sortedInter[key].pop()
                        res.append([key, tmp_key])
                    else:
                        break
            else:
                break
        return res



solution = Solution()
print(solution.criticalConnections(n, connections))


# 


