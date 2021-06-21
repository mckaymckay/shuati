#
# @lc app=leetcode.cn id=203 lang=python3
#
# [203] 移除链表元素
#


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        while head and head.val==val:
            head=head.next
        start=head
        if head:
            while start.next:
                if start.next.val==val:
                    start.next=start.next.next
                else:
                    start=start.next
            return head
        else:
            return 

        


# @lc code=end
