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
            "LEFT": [0,-1],
            "DOWN": [1,0],
            "RIGHT": [0,1],
            "UP": [-1,0]
        }

        current_position = [0,0]
        for index in commands:
            current_position = [current_position[0] + directions[index][0], current_position[1] + directions[index][1]]

        return current_position[0]*n + current_position[1]

# @lc code=end

# Time start: 12:32AM
# Time end: 1:00AM
