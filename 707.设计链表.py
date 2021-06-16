#
# @lc app=leetcode.cn id=707 lang=python3
#
# [707] 设计链表
#


# @lc code=start
class ListNode(object):
    def __init__(self, value=0):
        self.value = value
        self.next = None


class MyLinkedList:
    def __init__(self, value=0):
        self.head = None
        self.size = 0
        """
        Initialize your data structure here.
        """

    # 遍历
    def tranverse(self):
        start = self.head
        while start:  # 单链表的头指针为null时表示一个空链表
            print(start.value, '遍历')
            start = start.next

    def get(self, index: int) -> int:
        start = self.head
        if index < 0 or index >= self.size:
            return -1
        start = self.head
        for _ in range(index):
            start=start.next
        return start.value
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        """

    def addAtHead(self, val: int) -> None:
        self.addAtIndex(0, val)
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        """

    def addAtTail(self, val: int) -> None:
        self.addAtIndex(self.size, val)
        """
        Append a node of value val to the last element of the linked list.
        """

    def addAtIndex(self, index: int, val: int) -> None:
        if index > self.size:
            return
        newNode = ListNode(val)
        start = self.head
        if index <= 0:
            newNode.next = self.head
            self.head = newNode

        else:
            for _ in range(index - 1):
                start = start.next
            newNode.next = start.next
            start.next = newNode
        self.size += 1
        """
        Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted.
        """

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return
        start = self.head
        if index == 0:
            self.head = self.head.next
        else:
            start = self.head
            for _ in range(index - 1):
                start = start.next
            start.next = start.next.next
        self.size -= 1
        """
        Delete the index-th node in the linked list, if the index is valid.
        """


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
# @lc code=end
