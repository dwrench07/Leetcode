#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (63.30%)
# Likes:    14118
# Dislikes: 465
# Total Accepted:    5.8M
# Total Submissions: 8.6M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# 
# 
# Example 1:
# 
# 
# Input: s = "anagram", t = "nagaram"
# 
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: s = "rat", t = "car"
# 
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# 
# 
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # solution 1 - create a dict and store the values against it.
        # solution 2 - create an array and store values

        unique_characters = dict()
        for character in s:
            unique_characters[character] = unique_characters[character] + 1 if character in unique_characters else 1

        for character in t:
            unique_characters[character]  = unique_characters[character] - 1 if character in unique_characters else -1
        
        for character in unique_characters:
            if unique_characters[character] != 0:
                return False
        return True 

# @lc code=end

