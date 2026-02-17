#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#
# https://leetcode.com/problems/longest-consecutive-sequence/description/
#
# algorithms
# Medium (47.48%)
# Likes:    22679
# Dislikes: 1228
# Total Accepted:    3.1M
# Total Submissions: 6.7M
# Testcase Example:  '[100,4,200,1,3,2]'
#
# Given an unsorted array of integers nums, return the length of the longest
# consecutive elements sequence.
# 
# You must write an algorithm that runs in O(n) time.
# 
# 
# Example 1:
# 
# 
# Input: nums = [100,4,200,1,3,2]
# Output: 4
# Explanation: The longest consecutive elements sequence is [1, 2, 3, 4].
# Therefore its length is 4.
# 
# 
# Example 2:
# 
# 
# Input: nums = [0,3,7,2,5,8,4,6,0,1]
# Output: 9
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,0,1,2]
# Output: 3
# 
# 
# 
# Constraints:
# 
# 
# 0 <= nums.length <= 10^5
# -10^9 <= nums[i] <= 10^9
# 
# 
#

# @lc code=start
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # the logic is simple here 
        # store all the elements in a set first
        # then for every nums[i] check if nums[i]-1 exists, if yes, then skip
        # if it doesnot exist, then keep counting and store the max.
        unique_nums = set()
        max_count = 0
        for num in nums:
            unique_nums.add(num)
        
        for num in unique_nums:
            count = 0
            if num - 1 not in unique_nums:
                current = num
                while current in unique_nums:
                    current += 1
                    count += 1
            max_count = max(count, max_count)
        return max_count
# @lc code=end

