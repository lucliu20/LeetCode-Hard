# https://leetcode.com/problems/n-queens-ii/

"""
Example 1:
Input: n = 4
Output: 2
Explanation: There are two distinct solutions to the 4-queens puzzle as shown.

Example 2:
Input: n = 1
Output: 1
"""

n = 4


# Backtracking
# Recursively
# Strategy refers to:
# https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2654/
import collections
class Solution:
    def totalNQueens(self, n: int) -> int:
        def is_not_under_attack(r, c):
            if not self.d:
                return True
            for key, vals in self.d.items():
                can_r, can_c = key
                if can_r == r or can_c == c:
                    return False
                if (r,c) in vals:
                    return False
            return True

        def place_queen(r, c):
            for i, j in zip(range(r, n, 1), range(c, n, 1)):
                self.d[(r, c)].add((i, j))
            for i, j in zip(range(r, -1, -1), range(c, -1, -1)):
                self.d[(r, c)].add((i, j))
            for i, j in zip(range(r, -1, -1), range(c, n, 1)):
                self.d[(r, c)].add((i, j))
            for i, j in zip(range(r, n, 1), range(c, -1, -1)):
                self.d[(r, c)].add((i, j))

        def remove_queen(r, c):
            del self.d[(r,c)]

        def backtrack_nqueen(row = 0, count = 0):
            for col in range(n):
                # iterate through columns at the curent row.
                if is_not_under_attack(row, col):
                    # explore this partial candidate solution, and mark the attacking zone
                    place_queen(row, col)
                    if row + 1 == n:
                        # we reach the bottom, i.e. we find a solution!
                        count += 1
                    else:
                        # we move on to the next row
                        count = backtrack_nqueen(row + 1, count)
                    # backtrack, i.e. remove the queen and remove the attacking zone.
                    remove_queen(row, col)
            return count
        
        self.d = collections.defaultdict(set)
        return backtrack_nqueen(0, 0)

solution = Solution()
print(solution.totalNQueens(n))

# Runtime: 148 ms, faster than 15.86% of Python3 online submissions for N-Queens II.
# Memory Usage: 14.2 MB, less than 86.87% of Python3 online submissions for N-Queens II.

