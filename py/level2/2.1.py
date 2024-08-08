class DoublyLinkedList:
    class _Node:
        def __init__(self, value):
            self.value = value
            self.prev = None
            self.next = None

        def __str__(self):
            return str(self.value)

    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        return " <-> ".join(map(str, self))

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def add_first(self, value):
        new_node = self._Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def add_last(self, value):
        new_node = self._Node(value)
        if not self.tail:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete(self, value):
        current = self.head
        while current:
            if current.value == value:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                return
            current = current.next

    def __getitem__(self, value):
        for node in self:
            if node.value == value:
                return node
        return None

    def traverse_forward(self):
        print(f'Forward : {[str(i) for i in self]}')

    def traverse_backward(self):
        res = []
        current = self.tail
        while current:
            res.append(current)
            current = current.prev
        print(f'Backward: {[str(i) for i in res]}')


dll = DoublyLinkedList()

print("Список після додавання 1 2 3:")
dll.add_first(1)
dll.add_last(2)
dll.add_last(3)
print(dll)

dll.traverse_forward()
dll.traverse_backward()

print("Список після видалення 2:")
dll.delete(2)
print(dll)
