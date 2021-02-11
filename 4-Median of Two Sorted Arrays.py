# https://leetcode.com/problems/median-of-two-sorted-arrays/

"""
Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Example 3:
Input: nums1 = [0,0], nums2 = [0,0]
Output: 0.00000

Example 4:
Input: nums1 = [], nums2 = [1]
Output: 1.00000

Example 5:
Input: nums1 = [2], nums2 = []
Output: 2.00000
"""

nums1, nums2 = [1,3], [2]
# nums1, nums2 = [1,2], [3,4]
# nums1, nums2 = [0,0], [0,0]
# nums1, nums2 = [], [1]
# nums1, nums2 = [2], []


# Binary Search
# Time complexity: O(log (m+n))
class Solution:
    def findMedianSortedArrays(self, nums1: list(), nums2: list()) -> float:
        pass


solution = Solution()
print(solution.findMedianSortedArrays(nums1, nums2))

# 


