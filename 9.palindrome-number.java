/*
 * @lc app=leetcode id=9 lang=java
 *
 * [9] Palindrome Number
 */

// @lc code=start
class Solution {
    public boolean isPalindrome(int x) {
        /*
         * if x < 0 , return false
         * Solution 1: Convert to string
         * 
         * Solution 2: Solve as a number
         * 
         */
        int initial = x;
        int reverse = 0;
        if (x < 0)
            return false;
        else {
            while (x > 0) {
                reverse = reverse * 10 + x % 10;
                x = x / 10;
            }
        }
        return initial == reverse;
    }
}
// @lc code=end
