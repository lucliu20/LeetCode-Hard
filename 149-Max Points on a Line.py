# https://leetcode.com/problems/max-points-on-a-line/

"""
Example 1:
Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:
Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
"""


points = [[1,1],[2,2],[3,3]]
# points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]


from typing import List
import collections
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        res = 0
        for i in range(len(points)):
            mydict = collections.Counter()
            for j in range(i+1, len(points)):
                if points[i][0] - points[j][0] == 0:
                    k = float("inf")
                else:
                    k = (points[i][1] - points[j][1]) / (points[i][0] - points[j][0])
                mydict[k] += 1
                res = max(res, mydict[k])
        return res + 1

# Runtime: 52 ms, faster than 74.10% of Python3 online submissions for Max Points on a Line.
# Memory Usage: 14.2 MB, less than 93.62% of Python3 online submissions for Max Points on a Line.


solution = Solution()
print(solution.maxPoints(points))
