class Node(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class DoubleLinkedList(object):
    def __init__(self):
        self.head = None

    def append(self, node):
        if self.head:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = node
            node.prev = cur
        else:
            self.head = node

    def insertNodeAtIndex(self,idx,node):
        prev = None
        next = None

        if idx == 0:
            if self.head:
                next = self.head
                self.head = node
                self.head.next = next
                next.prev = self.head
            else:
                self.head = node
        else:
            cur_i = 0
            cur = self.head
            while cur_i < idx:
                if cur:
                    prev = cur
                    cur = cur.next
                else:
                    break;
                cur_i += 1
            if cur_i == idx:
                node.prev = prev
                node.next = cur
                prev.next = node
                if cur:
                    cur.prev = node
            else:
                print(-1)
                return -1

    def getDataIndex(self, data):
        cur = self.head
        cur_i = 0
        while cur:
            if cur.data == data:
                return cur_i
            else:
                cur = cur.next
                cur_i+=1
        print(-1)
        return -1

    def insertNodeAtData(self, data, node):
        index = self.getDataIndex(data)
        if index == -1:
            return -1
        else:
            self.insertNodeAtIndex(index, node)

    def deleteAtIndex(self, idx):
        next = None
        prev = None
        if idx == 0:
            if self.head:
                self.head = self.head.next
                self.head.prev = None
                return
            else:
                print(-1)
                return -1

        else:
            cur_i = 0
            cur = self.head
            while cur:
                if cur.next:
                    prev = cur
                    cur = cur.next
                    next = cur.next
                else:
                    break
                cur_i += 1
            if cur_i == idx:
                if next:
                    next.prev = prev
                prev.next = next
            else:
                print(-1)
                return -1
    def print(self):
        cur = self.head
        string = ''
        prev = None
        while cur:
            string += str(cur.data)
            if cur.next and cur.prev == prev:
                string += "<->"
            prev = cur
            cur = cur.next
        print(string)

if __name__ == "__main__":
    dl = DoubleLinkedList()
    dl.append(Node(1))
    dl.append(Node(2))
    dl.append(Node(3))
    dl.append(Node(4))
    dl.append(Node(6))
    dl.print()
    dl.insertNodeAtIndex(5, Node(7))
    dl.print()
    dl.insertNodeAtData(6,Node(5))
    dl.print()
    dl.deleteAtIndex(6)
    dl.print()