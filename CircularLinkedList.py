class SingleNode(object):
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head:
            curn = self.head
            while curn.next:
                curn = curn.next
            curn.next = node
            node.next = self.head
        else:
            self.head = node
            node.next = self.head

    def removeData(self, data):
        curn = self.head.next
        prev = self.head

        if self.head.data == data:

            while curn != self.head:
                prev = curn
                curn = curn.next

            prev.next = curn.next
            self.head = curn.next
        while curn != self.head:
            if curn.data == data:
                prev.next = curn.next
                return
            prev = curn
            curn = curn.next
        return -1

