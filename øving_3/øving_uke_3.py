class MyNode(object):
    def __init__(self, data=None, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev


# Doubly linked list
class MyLinkedList(object):
    def __init__(self):
        self.head = None    # first node in the list
        self.tail = None    # last node in the list
        self.size = 0

    def append(self, data):
        # Encapsulate the data in a MyNode
        new_node = MyNode(data, None, None)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
            self.count += 1

    def len(self):
        return self.size

    def iter(self):
        current = self.tail
        while current:
            val = current.data
            current = current.next
            yield val

    def delete_item(self, data):
        current = self.head
        node_deleted = False
        if current is None:
            node_deleted = False
        elif current.data == data:
            self.head = current.next
            self.head.prev = None
            node_deleted = True
        elif self.tail.data == data:    # item found at end of list
            self.tail = self.tail.prev
            self.tail.next = None
            node_deleted = True
        else:
            while current:
                if current.data == data:
                    current.prev.next = current.next
                    current.next.prev = current.prev
                    node_deleted = True
                current = current.next
        if node_deleted:
            self.count -= 1

    def contains(self, item):
        for node in self.iter():
            if item.data == node:
                return True
        return False


# Working Stack (MyLinkedList currently not implemented)
class MyStack:
    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, data):
        node = MyNode(data)
        if self.top:
            node.next = self.top
            self.top = node
        else:
            self.top = node
        self.size += 1

    def pop(self):
        if self.top:
            data = self.top.data
            self.size -= 1
            if self.top.next:
                self.top = self.top.next
            else:
                self.top = None
            return data
        else:
            return None

    def peek(self):
        if self.top:
            return self.top.data
        else:
            return None


myList = MyLinkedList()
stack = MyStack()
stack.push(1)
stack.push(2)
print(myList.len())
print(stack.pop())
print(stack.pop())
print(stack.pop())
