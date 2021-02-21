# https://leetcode.com/problems/n-queens/

"""
Example 1:
Input: n = 4
Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above

Example 2:
Input: n = 1
Output: [["Q"]]
"""

n = 4
# [[".Q..","...Q","Q...","..Q."],
#  ["..Q.","Q...","...Q",".Q.."]]

# Backtracking
# Recursively
# Strategy refers to:
# https://leetcode.com/explore/learn/card/recursion-ii/472/backtracking/2654/
import collections
class Solution:
    def solveNQueens(self, n: int) -> list(list()):
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
        
        def placement():
            solution = []
            for key, i in zip(self.d.keys(), range(n)):
                chars = ""
                qr, qc = key
                for j in range(n):
                    if qr == i and qc == j:
                        chars += "Q"
                    else:
                        chars += "."
                solution.append(chars)
            self.res.append(solution)

        def backtrack_nqueen(row = 0):
            for col in range(n):
                # iterate through columns at the curent row.
                if is_not_under_attack(row, col):
                    # explore this partial candidate solution, and mark the attacking zone
                    place_queen(row, col)
                    if row + 1 == n:
                        # we reach the bottom, i.e. we find a solution!
                        # count += 1
                        placement()
                    else:
                        # we move on to the next row
                        backtrack_nqueen(row + 1)
                    # backtrack, i.e. remove the queen and remove the attacking zone.
                    remove_queen(row, col)
            # return count
        
        self.d = collections.defaultdict(set)
        self.res = []
        backtrack_nqueen(0)
        return self.res

solution = Solution()
print(solution.solveNQueens(n))

# Runtime: 160 ms, faster than 20.52% of Python3 online submissions for N-Queens.
# Memory Usage: 14.8 MB, less than 54.28% of Python3 online submissions for N-Queens.

