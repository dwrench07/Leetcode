/*
 * @lc app=leetcode id=20 lang=java
 *
 * [20] Valid Parentheses
 */

// @lc code=start

import java.util.Stack;

class Solution {
    public boolean isValid(String s) {
        /*
         * is the count even, else return false
         * stack -> check the peek
         */
        if (s.length() % 2 != 0 || s.length() == 0)
            return false;
        Stack<Character> stack = new Stack<>();
        for (int position = 0; position < s.length(); position++) {
            if (s.charAt(position) == '(' ||
                    s.charAt(position) == '{' ||
                    s.charAt(position) == '[') {
                stack.push(s.charAt(position));
            } else if (!stack.isEmpty() &&
                    s.charAt(position) == ')' &&
                    stack.peek() == '(') {
                stack.pop();
            } else if (!stack.isEmpty() &&
                    s.charAt(position) == '}' &&
                    stack.peek() == '{') {
                stack.pop();
            } else if (!stack.isEmpty() &&
                    s.charAt(position) == ']' &&
                    stack.peek() == '[') {
                stack.pop();
            } else {
                return false;
            }
        }
        return stack.isEmpty();

    }
}
// @lc code=end
