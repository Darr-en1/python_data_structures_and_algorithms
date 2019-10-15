# 可迭代类（class collections.abc.Iterable）
# 提供__iter__()或者 提供__getitem __() 方法的类，都是可迭代类
# __iter__() 定义


class Array:
    def __init__(self, size=32, init=None):
        self._size = size
        self._items = [init] * size

    def __getitem__(self, item):
        return self._items[item]

    def __setitem__(self, key, value):
        self._items[key] = value

    def __len__(self):
        return len(self._items)

    def __str__(self):
        return str(self._items)

    def __delitem__(self, key):
        del self._items[key]

    def __iter__(self):
        for item in self._items:
            yield item


def test_array():
    a = Array(10, 1)
    assert len(a) == 10
    del a[2]
    assert len(a) == 9
    assert a[0] == 1
