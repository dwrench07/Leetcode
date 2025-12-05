#
# @lc app=leetcode id=20 lang=python
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s)%2 != 0:
            return False
        if len(s) == 0:
            return False
        
        parantheses = {
            '[': ']',
            '{': '}',
            '(': ')'
        }

        stack = []
        
        for character in s:
            if len(stack) == 0 and character not in parantheses.keys():
                return False
            elif len(stack) > 0 and parantheses[stack[-1]] == character:
                stack.pop()
            elif character in parantheses:
                stack.append(character)
            else:
                return False
        return len(stack) == 0

          



# @lc code=end
