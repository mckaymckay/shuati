#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        pa=headA
        pb=headB
        if pa and pb:
            while pa !=pb:
                pa=pa.next if pa else headB
                pb=pb.next if pb else headA
            return pa
        else:
            return None

        
        
# @lc code=end

