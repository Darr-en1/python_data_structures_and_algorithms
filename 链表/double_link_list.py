class Node(object):
    def __init__(self, value=None, prev=None, next=None):
        self.value, self.prev, self.next = value, prev, next

    def __str__(self):
        return f"{self.__class__}: {self.value}"


class CircularDoubleLinkedList(object):
    def __init__(self, maxsize=20):
        self.maxsize = maxsize if type(maxsize) == int else 20
        node = Node()
        node.next, node.prev = node, node
        self.root = node
        self.length = 0

    def __len__(self):
        return self.length

    def __str__(self):
        return f"{self.__class__}: {self.tolist()}"

    @property
    def headnode(self):
        return self.root.next

    @property
    def tailnode(self):
        return self.root.prev

    def append(self, value):
        self.is_full()
        node = Node(value, prev=self.tailnode, next=self.root)
        self.tailnode.next = node
        self.root.prev = node
        self.length += 1

    def pop(self):

        tailnode = self.tailnode

        if tailnode == self.root:
            raise Exception("Empty")

        tailnode.prev.next = self.root
        self.root.prev = tailnode.prev
        self.length -= 1

    def pop_left(self):

        headnode = self.headnode

        if headnode == self.root:
            raise Exception("Empty")

        headnode.next.prev = self.root
        self.root.next = headnode.next
        self.length -= 1

    def append_left(self, value):

        if self.root.next is self.root:
            return self.append(value)

        self.is_full()

        headnode = self.headnode

        node = Node(value, prev=self.root, next=headnode)
        self.root.next = node
        headnode.prev = node

        self.length += 1

    def remove(self, node):
        if node is self.root:
            return

        node.prev.next = node.next
        node.next.prev = node.prev
        self.length -= 1
        del node
        return 1

    def iter_node_reverse(self):
        if self.root.prev is self.root:
            return

        node = self.root.prev

        while node is not None and node != self.headnode:
            yield node
            node = node.prev
        yield node

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node(self):

        if self.root.next is self.root:
            return

        node = self.root.next

        while node is not None and node != self.tailnode:
            yield node
            node = node.next
        yield node

    def tolist(self):
        return [i for i in self]

    def is_full(self):
        if len(self) > self.maxsize:
            raise Exception("Full")


def test_append():
    cdl = CircularDoubleLinkedList()
    cdl.append(2)
    assert cdl.tolist() == [2]
    cdl.append(5)
    assert cdl.tolist() == [2, 5]
    cdl.append_left(5)
    assert cdl.tolist() == [5, 2, 5]


def test_append_left():
    cdl = CircularDoubleLinkedList()
    cdl.append_left(10)
    assert cdl.tolist() == [10]
    cdl.append_left(2)
    assert cdl.tolist() == [2, 10]


def test_remove():
    cdl = CircularDoubleLinkedList()

    assert cdl.remove(cdl.headnode) is None

    cdl.append_left(10)
    cdl.append_left(2)

    assert cdl.tolist() == [2, 10]

    assert cdl.remove(cdl.headnode) == 1

    assert cdl.tolist() == [10]


def test_iter_node_reverse():
    cdl = CircularDoubleLinkedList()

    cdl.append_left(10)
    cdl.append_left(2)
    cdl.append(5)
    cdl.append_left(2)
    cdl.append(12)

    assert cdl.tolist() == [2, 2, 10, 5, 12]

    assert [node.value for node in cdl.iter_node_reverse()] == [12, 5, 10, 2, 2]


def test_pop():
    cdl = CircularDoubleLinkedList()

    # cdl.pop()

    cdl.append_left(10)
    cdl.append_left(2)
    cdl.append(5)
    cdl.append_left(2)
    cdl.append(12)

    assert cdl.tolist() == [2, 2, 10, 5, 12]

    cdl.pop()
    assert cdl.tolist() == [2, 2, 10, 5]

    cdl.pop()
    assert cdl.tolist() == [2, 2, 10]

    cdl.pop()
    assert cdl.tolist() == [2, 2]

    cdl.pop()
    assert cdl.tolist() == [2]

    cdl.pop()
    assert cdl.tolist() == []


def test_pop_left():
    cdl = CircularDoubleLinkedList()

    # cdl.pop()

    cdl.append_left(10)
    cdl.append_left(2)
    cdl.append(5)
    cdl.append_left(2)
    cdl.append(12)

    assert cdl.tolist() == [2, 2, 10, 5, 12]

    cdl.pop_left()
    assert cdl.tolist() == [2, 10, 5, 12]

    cdl.pop_left()
    assert cdl.tolist() == [10, 5, 12]

    cdl.pop_left()
    assert cdl.tolist() == [5, 12]

    cdl.pop_left()
    assert cdl.tolist() == [12]

    cdl.pop_left()
    assert cdl.tolist() == []
