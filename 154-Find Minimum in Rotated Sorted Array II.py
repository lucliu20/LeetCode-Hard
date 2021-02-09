# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/

"""
Example 1:
Input: [1,3,5]
Output: 1

Example 2:
Input: [2,2,2,0,1]
Output: 0
"""

# nums = [1,3,5]
# nums = [2,2,2,0,1]
# nums = [2,2,2,0,1,2]
# nums = [1,3,3]
nums = [10,1,10,10,10]


# When num[mid] and num[right] are same, we are not sure the position of minimum in mid's left or right, so just let upper bound reduce by one.
# Also note that the we are comparing the num[mid] with the nums[right]; the nums[right] is the last element in the comparing window, and it changes every time.
# Time Complexcity O(log N)
class Solution:
    def findMin(self, nums: list()) -> int:
        left, right = 0, len(nums)-1
        while left < right:
            mid = left + (right-left) // 2
            if nums[mid] < nums[right]:
                right = mid
            elif nums[mid] > nums[right]:
                left = mid + 1
            elif nums[mid] == nums[right]:
                right -= 1
        return nums[left]


solution = Solution()
print(solution.findMin(nums))

# Runtime: 52 ms, faster than 72.14% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.
# Memory Usage: 14.9 MB, less than 48.32% of Python3 online submissions for Find Minimum in Rotated Sorted Array II.

