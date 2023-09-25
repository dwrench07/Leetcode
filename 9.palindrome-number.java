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
         * if the length is even:
         * compare first to last
         * till the half
         * if the length is odd:
         * compare till the middle, and leave
         * the middle number.
         * Solution 2: Solve as a number
         * General method using the while
         */
        if (x < 0)
            return false;
        String input = String.valueOf(x);
        int counter = 0;
        while (counter <= (input.length() / 2 - 1)) {
            if (input.charAt(counter) == (input.charAt(input.length() - 1 - counter))) {
                counter++;
            } else {
                return false;
            }
        }
        return true;
        // int initial = x;
        // int reverse = 0;
        // while (x > 0) {
        // reverse = reverse * 10 + x % 10;
        // x = x / 10;
        // }
        // return initial == reverse;
    }
}
// @lc code=end
