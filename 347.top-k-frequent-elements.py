#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (63.13%)
# Likes:    19284
# Dislikes: 850
# Total Accepted:    3.4M
# Total Submissions: 5.2M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,1,1,2,2,3], k = 2
# 
# Output: [1,2]
# 
# 
# Example 2:
# 
# 
# Input: nums = [1], k = 1
# 
# Output: [1]
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,2,1,2,1,2,3,1,3,2], k = 2
# 
# Output: [1,2]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# 
# 
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
# 
#

# @lc code=start
from collections import defaultdict
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        unique_nums = defaultdict(int)
        for num in nums:
            unique_nums[num] = unique_nums[num] + 1 if unique_nums[num] else 1
        heap = heapq.heapify()
        for unique_num in unique_nums:
            heapq.push(heap, (-unique_nums[unique_num], unique_num))
        output = []
        for _ in range(0,k):
            output.append(heapq.heappop(heap)[1])
        return output

        
# @lc code=end

