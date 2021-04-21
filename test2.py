class ListNode(object):
    def __init__(self, value=0):
        self.value = value
        self.next = None


class myList(object):
    def __init__(self):
        self._head = None

    def removeElement(self, head,val):
        start = self._head
        while start and start.value == val:
            start = start.next
        if start is None:
            return
        while start is not None:
            if start.next.value == val:
                start.next = start.next.next
            else:
                start = start.next
        return start
