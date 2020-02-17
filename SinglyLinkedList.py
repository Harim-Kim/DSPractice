class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyLinkedList(object):
    def __init__(self):
        self.head = None
        self.count = 0

    def append(self, node):
        if self.head == None:
            self.head = node
        else:
            cur = self.head
            while cur.next != None:
                cur = cur.next
            cur.next = node

    def getDataIndex(self,data):
        cur = self.head
        inx = 0
        while cur:
            if cur.data == data:
                return inx
            cur = cur.next
            inx += 1
        return -1

    def insertNodeAtIndex(self, idx, node):
        cur = self.head
        prev = None
        cur_i = 0

        if idx == 0:
            if self.head:
                push = self.head
                self.head = node
                self.head.next = push
            else:
                self.head =  node
        else:
            while cur_i < idx:
                if cur:
                    prev = cur
                    cur = cur.next
                else:
                    break
                cur_i += 1
            if cur_i == idx:
                node.next = cur
                prev.next = node
            else:
                return -1

    def insertNodeAtData(self,data,node):
        index = self.getDataIndex(data)
        if 0 <= index:
            self.insertNodeAtData(index, node)
        else:
            return -1

    def deleteAtIndex(self, idx):
        cur_i = 0
        cur = self.head
        prev = None
        next = self.head.next
        if idx == 0:
            self.head = next
        else:
            while cur_i < idx:
                if cur.next:
                    prev = cur
                    next = next.next
                else:
                    break
                cur_i += 1
            if cur_i == idx:
                prev.next = next
            else:
                return -1

    def clear(self):
        self.head = None

    def print(self):
        cur = self.head
        print_string = ""
        while cur:
            print_string += str(cur.data)
            if cur.next:
                print_string += "->"
            cur = cur.next
        print(print_string)

if __name__ == "__main__":
    sl = SinglyLinkedList()
    sl.append(Node(1))
    sl.append(Node(2))
    sl.append(Node(3))

    sl.append(Node(5))
    sl.insertNodeAtIndex(3, Node(4))
    sl.print()
    print(sl.getDataIndex(1))
    print(sl.getDataIndex(2))
    print(sl.getDataIndex(3))
    print(sl.getDataIndex(4))
    print(sl.getDataIndex(5))
    sl.insertNodeAtData(1, Node(0))
    sl.print()
exit()