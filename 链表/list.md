## 单链表
因为array是内存连续的，在删除连接节点时，其他位置节点也会发生变动，
链式结构内存不连续的，链表的特性完美的解决了这一问题，
但是他的find时间复杂度为O(n)，单链表的remove 需要遍历获取上一个节点，因此remove也是O(n)


链表操作 | 平均时间复杂度
---- | ---
lls.append(value) | O(1)
lls.append_left(value) | O(1)
lls.pop_left(value) | O(1)
lls.find(value) | O(n)
lls.remove(value) | O(n)


## 双链表
双链表不同于单链表，它会记录当前节点的上一个节点,因此可以做到很多的操作时间复杂度都能降为O(1)

循环双端链表操作 | 平均时间复杂度
---- | ---
cdl.append(value) | O(1)
cdl.append_left(value) | O(1)
cdl.pop(value) | O(1)
cdl.pop_left(value) | O(1)
cdl.remove(node) | O(1)
cdl.headnode | O(1)
cdl.tailnode | O(1)
