# 定义结点
class Node(object):
    def __init__(self, value=0):
        self.value = value
        self.next = None


# 定义链表
class SingleList(object):
    def __init__(self):
        self._head = None

    def append(self, data):
        start = self._head
        item = Node(data)
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

    def removeElement(self, head, val):
        # 删除等于val的首元结点
        while head._head and head._head.value == val:
            head._head = head._head.next
        if head._head is None:
            return
        start=head._head
        # 删除等于val的非首元结点
        while start.next is not None:
            if start.next.value == val:
                start.next = start.next.next
            else:
                start = start.next
        return head


arr = [2, 2, 2]
mylist = SingleList()
for i in arr:
    mylist.append(i)
mylist.removeElement(mylist, 2)
mylist.tranverse()
