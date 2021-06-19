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
        if l1 and l2:
            pre = ListNode()
            prehead=pre
            curr1 = l1
            curr2 = l2
            while curr1 and curr2:
                if curr1.val > curr2.val:
                    prehead.next = curr2
                    curr2=curr2.next
                else:
                    prehead.next=curr1
                    curr1=curr1.next
                prehead=prehead.next

            # if not curr1:
            #     prehead.next=curr2
            # else:
            #     prehead.next=curr1
            prehead.next=curr1 if curr2==None else curr2
            return pre.next

        else:
            return l2 if l1 is None else l1


# @lc code=end
