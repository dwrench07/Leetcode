/*
 * @lc app=leetcode id=13 lang=java
 *
 * [13] Roman to Integer
 */

// @lc code=start
class Solution {
    public int romanToInt(String s) {
        /*
         * wite a for loop to loop through the integer
         * store the previous value, and the current
         * compare current with previous
         * if current is greater than previous,
         * subtract current from answer
         */
        int value = 0;
        int current = 0, previous = 0;
        for (int pointer = s.length() - 1; pointer >= 0; pointer--) {
            switch (s.charAt(pointer)) {
                case 'I':
                    current = 1;
                    break;
                case 'V':
                    current = 5;
                    break;
                case 'X':
                    current = 10;
                    break;
                case 'L':
                    current = 50;
                    break;
                case 'C':
                    current = 100;
                    break;
                case 'D':
                    current = 500;
                    break;
                case 'M':
                    current = 1000;
                    break;
            }
            if (current < previous) {
                value -= current;
            } else {
                value += current;
            }
            previous = current;
        }
        return value;
    }
}
// @lc code=end
