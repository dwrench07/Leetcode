#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#
# https://leetcode.com/problems/container-with-most-water/description/
#
# algorithms
# Medium (54.15%)
# Likes:    33762
# Dislikes: 2172
# Total Accepted:    5.1M
# Total Submissions: 8.5M
# Testcase Example:  '[1,8,6,2,5,4,8,3,7]'
#
# You are given an integer array height of length n. There are n vertical lines
# drawn such that the two endpoints of the i^th line are (i, 0) and (i,
# height[i]).
# 
# Find two lines that together with the x-axis form a container, such that the
# container contains the most water.
# 
# Return the maximum amount of water a container can store.
# 
# Notice that you may not slant the container.
# 
# 
# Example 1:
# 
# 
# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array
# [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the
# container can contain is 49.
# 
# 
# Example 2:
# 
# 
# Input: height = [1,1]
# Output: 1
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 2 <= n <= 10^5
# 0 <= height[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        # Note, this is similar to 2 sum
        left,right = 0,len(height)-1
        max_area = 0
        while left < right:
            area =  height[left] * (right-left) if height[left] < height[right] else height[right] * (right-left)
            max_area = max(max_area,area)
            if height[left] < height[right]:
                left += 1
            elif height[left] > height[right] :
                right -= 1
            else:
                left += 1
                right -= 1
        return max_area
# @lc code=end

