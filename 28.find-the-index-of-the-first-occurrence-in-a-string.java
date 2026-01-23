/*
 * @lc app=leetcode id=28 lang=java
 *
 * [28] Find the Index of the First Occurrence in a String
 */

// @lc code=start
class Solution {
    public int strStr(String haystack, String needle) {
        int counter = needle.length();
        int location = -1;
        for (int position = 0; position < haystack.length(); position++) {
            if (counter == 0)
                break;
            else if (haystack.charAt(position) == needle.charAt(0) && counter == needle.length()) {
                counter--;
                location = position;
            } else if (haystack.charAt(position) == needle.charAt(needle.length() - counter)) {
                counter--;
            } else {
                counter = needle.length();
                location = -1;
            }
        }
        return counter == 0 ? location : -1;
    }
}
// @lc code=end
