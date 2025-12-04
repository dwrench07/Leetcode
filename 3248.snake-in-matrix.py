#
# @lc app=leetcode id=3248 lang=python
#
# [3248] Snake in Matrix
#

# @lc code=start
class Solution(object):
    def finalPositionOfSnake(self, n, commands):
        """
        :type n: int
        :type commands: List[str]
        :rtype: int
        """
        directions = {
            "LEFT": -1,
            "DOWN": n,
            "RIGHT": 1,
            "UP": -n
        }

        current_position = 0
        for command in commands:
            current_position = current_position + directions[command]

        return current_position

# @lc code=end

# Time start: 01:02AM
# Time end: 01:04AM
