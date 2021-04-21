# 结点定义
class ListNode(object):
    def __init__(self, value=0):
        self.value = value
        self.next = None


# 链表定义
class Mylist(object):
    def __init__(self):
        self._head = None
        self.size = 0

    def append(self, data):
        start = self._head
        item = ListNode(data)
        self.size += 1
        if start is None:
            self._head = item
            return
        while start.next is not None:
            start = start.next
        start.next = item

    # 遍历
    def tranverse(self):
        start = self._head
        while start is not None:
            print(start.value, '**')
            start = start.next

    # 获取链表
    def get(self, index):
        start = self._head
        if index < 0 or index >= self.size:
            return -1
        if index == 0:
            return self._head.value
        for _ in range(index):
            start = start.next
        return start.value

    # 首元结点前插入值
    def addAtHead(self, data):
        item = ListNode(data)
        self.size += 1
        # if self._head is None:
        #     self._head = item
        # else:
        item.next = self._head  ###########
        self._head = item

    # 在结尾插入值
    def addAtTail(self,data):
        self.append(data)
    
    # 在index处插入结点
    def addAtIndex(self,index,data):
        if index>self.size:
            return
        self.size+=1
        item=ListNode(data)
        if index<=0:
            # self.addAtHead(data)
            item.next=self._head
            self._head
        else:
            start=self._head
            for _ in range(index-1):
                start=start.next
            item.next=start.next
            start.next=item

    # 删除index处的值
    def deleteAtIndex(self,index):
        if index<0 or index>=self.size:
            return
        self.size-=1
        if index==0:
            self._head=self._head.next
        else:
            pre=self._head
            for _ in range(index-1):
                pre=pre.next
            pre.next=pre.next.next




arr = [1, 2, 3]
MyFirstList = Mylist()

for i in arr:
    MyFirstList.append(i)
print(MyFirstList._head, '333')
MyFirstList.addAtHead(5)
MyFirstList.addAtTail(6)
MyFirstList.addAtIndex(1,7)
MyFirstList.addAtIndex(4,8)
MyFirstList.deleteAtIndex(6)
MyFirstList.tranverse()
print('size', MyFirstList.size)
print(MyFirstList.get(0))