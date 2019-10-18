class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        return f"{self.__class__}: {self.value}"


class LinkedList:
    def __init__(self, maxsize=20):
        self.maxsize = maxsize if type(maxsize) == int else 20
        self.root = Node()
        self.length = 0
        self.tail_node = None

    def __len__(self):
        return self.length

    def __str__(self):
        return f"{self.__class__}: {self.tolist()}"

    def __iter__(self):
        for node in self.iter_node():
            yield node.value

    def iter_node(self):
        node = self.root.next
        while node:
            yield node
            node = node.next

    def append(self, value):
        self.is_full()
        node = Node(value)
        if self.tail_node is None:
            self.root.next = node
        else:
            self.tail_node.next = node
        self.tail_node = node
        self.length += 1

    def append_left(self, value):
        self.is_full()
        node = Node(value)
        node.next = self.root.next
        self.root.next = node
        self.length += 1

    def remove(self, value):
        prev_node = self.root
        node = self.root.next
        while type(node) == Node:
            if node.value == value:
                prev_node.next = node.next
                if node == self.tail_node:
                    self.tail_node = prev_node
                del node
                self.length -= 1
                return
            else:
                prev_node = node
                node = node.next
        return -1

    def pop_left(self):
        headnode = self.root.next
        if headnode is None:
            raise Exception("pop from empty LinkedList")

        self.root.next = headnode.next
        if self.tail_node == headnode:
            self.tail_node = None

        del headnode
        self.length -= 1

    def clear(self):
        for node in self.iter_node():
            del node
        self.root.next, self.tail_node = None, None
        self.length = 0

    def tolist(self):
        return [i for i in self]

    def find(self, value):
        return self.tolist().    index(value)

    def is_full(self):
        if len(self) > self.maxsize:
            raise Exception("Full")


def test_append():  # py.test LinkedList.py
    lls = LinkedList()
    lls.append(2)
    assert lls.tail_node.value == 2
    lls.append(5)

    assert lls.tail_node.value == 5

    assert len(lls) == 2

    assert [i for i in lls] == [2, 5]


def test_append_left():
    lls = LinkedList()
    lls.append(2)
    lls.append(5)
    lls.append_left(4)
    assert [i for i in lls] == [4, 2, 5]

    assert len(lls) == 3


def test_find():
    lls = LinkedList()
    lls.append(2)
    lls.append(5)
    lls.append_left(4)
    assert lls.find(4) == 0
    assert lls.find(5) == 2


def test_remove():
    lls = LinkedList()
    lls.append(2)
    lls.append(5)
    lls.append_left(4)
    lls.remove(5)
    assert [i for i in lls] == [4, 2]

    assert lls.tail_node.value == 2

    assert len(lls) == 2

    res = lls.remove(100)

    assert res == -1

    assert [i for i in lls] == [4, 2]

    assert lls.tail_node.value == 2

    assert len(lls) == 2

    res = lls.remove(4)

    assert res is None

    assert [i for i in lls] == [2]

    assert lls.tail_node.value == 2

    assert len(lls) == 1


def test_popleft():
    lls = LinkedList()
    lls.append(2)
    lls.append(5)
    lls.append_left(4)
    lls.pop_left()
    assert lls.tolist() == [2, 5]
    assert len(lls) == 2
    lls.pop_left()
    lls.pop_left()
    assert lls.tolist() == []
    assert len(lls) == 0
    assert lls.tail_node is None


def test_clear():
    lls = LinkedList()
    lls.append(2)
    lls.append(5)
    lls.append_left(4)
    lls.clear()
    assert lls.tolist() == []
    assert len(lls) == 0
    assert lls.tail_node is None
