/*
 * @lc app=leetcode id=21 lang=java
 *
 * [21] Merge Two Sorted Lists
 */

// @lc code=start
/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode mergeTwoLists(ListNode list1, ListNode list2) {
        /*
         * first check if any of them is null, if true
         * return non-empty
         * Check if any of the list is empty, else
         * Compare the element in each list
         * if empty - >
         */
        ListNode current = new ListNode();
        ListNode list3 = current;
        if (list1 == null)
            return list2;
        else if (list2 == null)
            return list1;
        else {
            while (list1 != null || list2 != null) {
                if (list1 == null) {
                    list3.next = list2;
                } else if (list2 == null) {
                    list3.next = list1;
                } else if (list1.val < list2.val) {
                    list3 = new ListNode(list1.val);
                    list3.next = new ListNode(list2.val);
                    list3 = list3.next;
                    list1 = list1.next;
                    list2 = list2.next;
                } else {
                    list3 = new ListNode(list2.val);
                    list3.next = new ListNode(list1.val);
                    list3 = list3.next;
                    list1 = list1.next;
                    list2 = list2.next;
                }
            }
        }
        return current;
    }
}
// @lc code=end
