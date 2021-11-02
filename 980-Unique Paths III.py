# https://leetcode.com/problems/unique-paths-iii/

"""
Example 1:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
Output: 2
Explanation: We have the following two paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2)
2. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2)

Example 2:
Input: grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
Output: 4
Explanation: We have the following four paths: 
1. (0,0),(0,1),(0,2),(0,3),(1,3),(1,2),(1,1),(1,0),(2,0),(2,1),(2,2),(2,3)
2. (0,0),(0,1),(1,1),(1,0),(2,0),(2,1),(2,2),(1,2),(0,2),(0,3),(1,3),(2,3)
3. (0,0),(1,0),(2,0),(2,1),(2,2),(1,2),(1,1),(0,1),(0,2),(0,3),(1,3),(2,3)
4. (0,0),(1,0),(2,0),(2,1),(1,1),(0,1),(0,2),(0,3),(1,3),(1,2),(2,2),(2,3)

Example 3:
Input: grid = [[0,1],[2,0]]
Output: 0
Explanation: There is no path that walks over every empty square exactly once.
Note that the starting and ending square can be anywhere in the grid.
"""


# grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]]
# grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
grid = [[0,1],[2,0]]



# Backtracking
from typing import List
class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        def isValid(r, c, memo):
            if r in range(len(grid)) and c in range(len(grid[0])):
                if grid[r][c] == 0 and (r,c) not in memo:
                    return True
            return False

        def foundSolution(memo, start):
            if empties + 1 == len(memo):
                directions = [(0,1), (1,0), (-1,0), (0,-1)]
                for d in directions:
                    row = d[0] + start[0]
                    col = d[1] + start[1]
                    if row in range(len(grid)) and col in range(len(grid[0])) and (grid[row][col] == 2):
                        return True
            return False

        def placing(r, c, memo):
            memo.add((r,c))

        def removing(r, c, memo):
            memo.remove((r,c))

        def backtracking(memo, start):
            if foundSolution(memo, start):
                self.res += 1
                return
            directions = [(0,1), (1,0), (-1,0), (0,-1)]
            for d in directions:
                row = d[0] + start[0]
                col = d[1] + start[1]
                if isValid(row, col, memo):
                    placing(row, col, memo)
                    backtracking(memo, (row,col))
                    removing(row, col, memo)

        self.res = 0
        memo = set()
        start, empties = tuple(), 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 0:
                    empties += 1
        memo.add(start)
        backtracking(memo, start)
        return self.res


# Runtime: 88 ms, faster than 38.45% of Python3 online submissions for Unique Paths III.
# Memory Usage: 14.4 MB, less than 15.62% of Python3 online submissions for Unique Paths III.


solution = Solution()
print(solution.uniquePathsIII(grid))
