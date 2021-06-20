# @before-stub-for-debug-begin
from python3problem21 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        pre = ListNode()
        prehead=pre
        while l1 and l2:
            if l1.val>l2.val:
                prehead.next=l2
                l2=l2.next
            else:
                prehead.next=l1
                l1=l1.next
            prehead=prehead.next
        prehead.next=l1 if l2==None else l2
        return pre.next


# @lc code=end
