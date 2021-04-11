# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/

"""
Example 1:
Input: matrix = [[9,9,4],[6,6,8],[2,1,1]]
Output: 4
Explanation: The longest increasing path is [1, 2, 6, 9].

Example 2:
Input: matrix = [[3,4,5],[3,2,6],[2,2,1]]
Output: 4
Explanation: The longest increasing path is [3, 4, 5, 6]. Moving diagonally is not allowed.

Example 3:
Input: matrix = [[1]]
Output: 1

"""


# matrix = [[9,9,4],[6,6,8],[2,1,1]]
# matrix = [[3,4,5],[3,2,6],[2,2,1]]
# matrix = [[1]]

# Test case 135, Expected: 140
matrix = [[0,1,2,3,4,5,6,7,8,9],[19,18,17,16,15,14,13,12,11,10],[20,21,22,23,24,25,26,27,28,29],[39,38,37,36,35,34,33,32,31,30],[40,41,42,43,44,45,46,47,48,49],[59,58,57,56,55,54,53,52,51,50],[60,61,62,63,64,65,66,67,68,69],[79,78,77,76,75,74,73,72,71,70],[80,81,82,83,84,85,86,87,88,89],[99,98,97,96,95,94,93,92,91,90],[100,101,102,103,104,105,106,107,108,109],[119,118,117,116,115,114,113,112,111,110],[120,121,122,123,124,125,126,127,128,129],[139,138,137,136,135,134,133,132,131,130],[0,0,0,0,0,0,0,0,0,0]]



# Back tracking
# 135 / 138 test cases passed.
# Status: Time Limit Exceeded
# from typing import List
# class Solution:
#     def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
#         def isValid(curr, candidate, visited):
#             if candidate[0] not in range(len(matrix)) or candidate[1] not in range(len(matrix[0])):
#                 return False
#             if (candidate[0], candidate[1]) in visited:
#                 return False
#             if matrix[candidate[0]][candidate[1]] <= matrix[curr[0]][curr[1]]:
#                 return False
#             return True
#         
#         def place(candidate, visited):
#             visited.add(candidate)
#             return
# 
#         def remove(candidate, visited):
#             visited.remove(candidate)
#             return
# 
#         def backtrack(row, col, path, visited):
#             # directions = [[1, 0], [-1, 0], [0, 1], [0, -1]] # down, up, right, and left
#             directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # right, down, left, and up 
#             longest = 0
#             for x, y in directions:
#                 if isValid((row, col), (row+x, col+y), visited):
#                     place((row+x, col+y), visited)
#                     longest = max(longest, backtrack(row+x, col+y, path+1, visited))
#                     remove((row+x, col+y), visited)
#             return max(longest, path)
#         
#         res, n, m = -float("inf"), len(matrix), len(matrix[0])
#         path, visited = 1, set()
#         for i in range(n):
#             for j in range(m):
#                 place((i, j), visited)
#                 res = max(res, backtrack(i, j, path, visited))
#                 remove((i, j), visited)
#         return res


# DFS + memoization: Time complexity: O(nm), space complexity: O(nm)
from typing import List
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        def isValid(curr, candidate):
            if candidate[0] not in range(len(matrix)) or candidate[1] not in range(len(matrix[0])):
                return False
            if matrix[candidate[0]][candidate[1]] <= matrix[curr[0]][curr[1]]:
                return False
            return True

        def helper(row, col):
            if dp[row][col] != 0:
                return dp[row][col]
            directions = [[0, 1], [1, 0], [0, -1], [-1, 0]] # right, down, left, and up 
            longest = 1
            for x, y in directions:
                if isValid((row, col), (row+x, col+y)):
                    longest = max(longest, helper(row+x, col+y)+1)
            dp[row][col] = longest
            return dp[row][col]
        
        res, n, m = -float("inf"), len(matrix), len(matrix[0])
        dp = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                res = max(res, helper(i, j))
        return res


solution = Solution()
print(solution.longestIncreasingPath(matrix))

# Runtime: 740 ms, faster than 8.43% of Python3 online submissions for Longest Increasing Path in a Matrix.
# Memory Usage: 15.2 MB, less than 74.81% of Python3 online submissions for Longest Increasing Path in a Matrix.

