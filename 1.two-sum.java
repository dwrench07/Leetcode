/*
 * @lc app=leetcode id=1 lang=java
 *
 * [1] Two Sum
 */

// @lc code=start
class Solution {
    public int[] twoSum(int[] nums, int target) {
        /*
         * subtract target - nums[i] and store result
         * check if the nums[i+1] is in the set
         * edge case:
         * store only till -> nums.length - 2
         */
        HashMap<Integer, Integer> hash = new HashMap<>();
        int first = 0, second = 0;
        for (int i = 0; i < nums.length; i++) {
            if (hash.containsKey(nums[i])) {
                second = i;
                first = hash.get(nums[i]);
                break;
            } else
                hash.put(target - nums[i], i);
        }
        return new int[] { first, second };
    }
}
// @lc code=end
