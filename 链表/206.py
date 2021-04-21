# 反转链表
class ListNode(object):
    def __init__(self, value=0):
        self.value = value
        self.next = None


class Solution(object):
    def __init__(self):
        self._head = None

    def append(self, data):
        start = self._head
        item = ListNode(data)
        if start is None:
            self._head = item
            return  #1
        while start.next is not None:  #2
            start = start.next
        start.next = item

    def tranverse(self):
        start = self._head
        while start is not None:
            print(start.value, '**')
            start = start.next

    # 双指针迭代法
    def reverseList(self, head):
        pre = None  #####这个结点必须指向none，否则链表中可能会产生环
        temp = ListNode()
        start = head._head
        if start is None:
            return
        while start.next is not None:
            temp = start.next
            start.next = pre
            pre = start
            start = temp
        start.next = pre
        head._head = start
        return head

    def reverse(self,head):
        start=head._head 
        if start is None:
            return 
        pre=None
        temp=ListNode()
        while start.next is not None:
            temp=start.next
            start.next=pre
            pre=start
            start=temp
        start.next=pre
        head._head=start
        return head




arr = [1, 2, 3, 4, 5]
mylist = Solution()
for i in arr:
    mylist.append(i)
mylist.tranverse()
print('------------')
mylist.reverseList(mylist)
mylist.tranverse()
print('------------')
mylist.reverse(mylist)
mylist.tranverse()
