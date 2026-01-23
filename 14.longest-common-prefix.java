/*
 * @lc app=leetcode id=14 lang=java
 *
 * [14] Longest Common Prefix
 */

// @lc code=start
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length == 1)
            return strs[0];
        int counter = 0;
        StringBuilder output = new StringBuilder();
        boolean isCommon = true;
        while (isCommon) {
            for (int i = 0; i < strs.length - 1; i++) {
                if (!((strs[i].length() - 1 >= counter &&
                        strs[i + 1].length() - 1 >= counter) &&
                        strs[i].charAt(counter) == strs[i + 1].charAt(counter))) {
                    isCommon = false;
                }
            }
            if (isCommon)
                output.append(strs[0].charAt(counter));
            counter++;
        }
        return output.toString();
    }
}
// @lc code=end
