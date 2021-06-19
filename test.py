# 设计链表


# 定义结点
class ListNode(object):
    def __init__(self, value=0):
        self.value = value
        self.next = None


# 定义链表
class MyLinkerList(object):
    def __init__(self):
        self.head = None
        self.size = 0

    # 遍历
    def tranverse(self):
        start = self.head
        while start:
            print(start.value, '@@')
            start = start.next

    # 获取链表中第 index 个节点的值。如果索引无效，则返回-1。
    def get(self, index):
        if index < 0 or index >= self.size:
            return -1
        start = self.head
        for i in range(index):  ###################
            start = start.next
        return start.value

    # 在开始插入结点
    def addAtHead(self, val):
        item = ListNode(val)
        item.next = self.head
        self.head = item
        self.size += 1

    # 在末尾插入结点
    def addAtTail(self, val):
        item = ListNode(val)
        start = self.head
        self.size += 1
        if start is None:
            self.head = item
            return  #############
        while start.next is not None:  ##################
            start = start.next
        start.next = item

    # 在链表中的第 index 个节点之前添加值为 val  的节点。如果 index 等于链表的长度，则该节点将附加到链表的末尾。
    # 如果 index 大于链表长度，则不会插入节点。如果index小于0，则在头部插入节点。
    def addAtIndex(self, index, val):
        item = ListNode(val)
        if index > self.size:
            return
        start = self.head
        self.size += 1
        if index <= 0:
            index = 0
            item.next = self.head
            self.head = item
        else:
            for _ in range(1, index):
                start = start.next
            item.next = start.next
            start.next = item

    # 删除index处的值:如果索引 index 有效，则删除链表中的第 index 个节点。
    def deleteAtIndex(self, index):
        if index < 0 or index >= self.size:
            return
        if index == 0:
            self.head = self.head.next
        else:
            start = self.head
            while (index - 1):
                start = start.next
                index -= 1
            start.next = start.next.next
        self.size -= 1

def mergeTwoLists(l1, l2):
    if l1 and l2:
        curr1 = l1
        curr2 = l2
        while curr1 and curr2:
            pre1 = curr1.next
            pre2 = curr2.next
            if curr1.val > curr2.val:
                curr2.next = curr1
                curr2 = pre2
            else:
                curr1.next = curr2
                curr1 = pre1
        if not curr1:
            # curr1.next = curr2
            return l2
        else:
            # curr2.next = curr1
            return l1
    else:
        return l2 if l1 is None else l1


l1 = [1, 2, 4]
l2 = [1, 3, 4]
mylist1 = MyLinkerList()
mylist2 = MyLinkerList()
# length = len(arr)
# for i in range(length):
mylist1.addAtIndex(0, 1)
mylist1.addAtIndex(1, 2)
mylist1.addAtIndex(2, 4)
mylist2.addAtIndex(0, 1)
mylist2.addAtIndex(1, 3)
mylist2.addAtIndex(2, 4)
print(mylist2.tranverse())
# print(mergeTwoLists(mylist1, mylist2))
