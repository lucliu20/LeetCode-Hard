# https://leetcode.com/problems/count-vowels-permutation/

"""
Example 1:
Input: n = 1
Output: 5
Explanation: All possible strings are: "a", "e", "i" , "o" and "u".

Example 2:
Input: n = 2
Output: 10
Explanation: All possible strings are: "ae", "ea", "ei", "ia", "ie", "io", "iu", "oi", "ou" and "ua".

Example 3: 
Input: n = 5
Output: 68
"""

# n = 1
# n = 2
# n = 3 # 19
n = 5



# DP
# Iteratively
class Solution:
    def countVowelPermutation(self, n: int) -> int:
        MAX = 10**9 + 7
        dp = [[0]*5 for _ in range(n)]
        # dp = [[0 for _ in range(5)] for _ in range(n)]
        for i in range(5):
            dp[0][i] = 1
        for i in range(1, n):
            for j in range(5):
                if j == 0: # ends with the "a" vowel, previous could be "e", "i", "u".
                    dp[i][j] = dp[i-1][1] + dp[i-1][2] + dp[i-1][4]
                elif j == 1: # ends with the "e" vowel, previous could be "a", "i".
                    dp[i][j] = dp[i-1][0] + dp[i-1][2]
                elif j == 2: # ends with the "i" vowel, previous could be "e", "o".
                    dp[i][j] = dp[i-1][1] + dp[i-1][3]
                elif j == 3: # ends with the "o" vowel, previous could be "i".
                    dp[i][j] = dp[i-1][2]
                elif j == 4: # ends with the "u" vowel, previous could be "i", "o".
                    dp[i][j] = dp[i-1][2] + dp[i-1][3]
        return sum(dp[n-1])%MAX

# Runtime: 480 ms, faster than 36.62% of Python3 online submissions for Count Vowels Permutation.
# Memory Usage: 117.5 MB, less than 20.52% of Python3 online submissions for Count Vowels Permutation.


# If using: dp = [[0 for _ in range(5)] for _ in range(n)]
# Runtime: 532 ms, faster than 33.51% of Python3 online submissions for Count Vowels Permutation.
# Memory Usage: 117.7 MB, less than 19.22% of Python3 online submissions for Count Vowels Permutation.


solution = Solution()
print(solution.countVowelPermutation(n))


