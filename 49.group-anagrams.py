#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (66.96%)
# Likes:    21821
# Dislikes: 748
# Total Accepted:    4.5M
# Total Submissions: 6.3M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
# 
# 
# Example 1:
# 
# 
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# 
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# 
# Explanation:
# 
# 
# There is no string in strs that can be rearranged to form "bat".
# The strings "nat" and "tan" are anagrams as they can be rearranged to form
# each other.
# The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to
# form each other.
# 
# 
# 
# Example 2:
# 
# 
# Input: strs = [""]
# 
# Output: [[""]]
# 
# 
# Example 3:
# 
# 
# Input: strs = ["a"]
# 
# Output: [["a"]]
# 
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
# 
# 
#

# @lc code=start
from collections import Counter
from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # hash_store = {}

        # for element in strs:
        #     array = []
        #     for i in range(len(element)):
        #         array.append(element[i])
        #     array.sort()
        #     string = "".join(array)
        #     if string in hash_store:
        #         hash_store[string].append(element)
        #     else:
        #         hash_store[string] = [element]
            
        # output = []
        # for element in hash_store.values():
        #     output.append(element)
        # return output

        '''
        strs -> strings
        output -> anagrams
        '''
        # output = []
        # output_dictionary = defaultdict(list)
        # for string in strs:
        #     character_dictionary = Counter(string)
        #     sorted_string = [char * character_dictionary[char] for char in character_dictionary]
        #     sorted_string.sort()

        #     output_dictionary["".join(sorted_string)].append(string)
        # output = list(output_dictionary.values())
        # return  output

        '''
        Another approach is
        '''
        output = []
        output_dictionary = defaultdict(list)
        for string in strs:
            sorted_chars = sorted(string)
            output_dictionary["".join(sorted_chars)].append(string)
        output = list(output_dictionary.values())
        return output        
# @lc code=end

