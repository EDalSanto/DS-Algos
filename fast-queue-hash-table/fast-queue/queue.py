class PythonListQueue(object):
    """
    A queue based on the built in Python list type.
    """
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        return self._items.pop(0)

    def size(self):
        return len(self._items)

    def is_empty(self):
        return len(self._items) == 0


class LinkedListNode(object):
    """
    A doubly linked list node, support for the LinkedListQueue. You should not need
    to change this code, but you will want to use it in the LinkedListQueue
    """
    def __init__(self, value, prevNode, nextNode):
        self.value = value
        self.prev = prevNode
        self.next = nextNode

class LinkedListQueue(object):
    """
    This list enqueues to the tail and dequeues from the head.
    Uses a doubly linked list to ensure O(1) time enqueue and dequeue.
    """
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def enqueue(self, item):
        # Enqueue to tail
        new_node = LinkedListNode(item, self._tail, None)

        # Initialize list head and nexts
        if self._size == 0:
            self._head = new_node
        elif self._size == 1:
            self._head.next = new_node
        else:
            self._tail.next = new_node

        # Point tail to new_node
        self._tail = new_node
        self._size += 1

    def dequeue(self):
        node_to_return = self._head
        new_head = node_to_return.next

        if new_head:
            new_head.prev = None

        self._head = new_head
        self._size -= 1

        return node_to_return.value

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0

class RingBufferQueue:
    '''
    Finish the functions below such that this queue is backed by a Ring Buffer.
    Recall that a ring buffer uses an array and two pointers to keep track of
    where to read, and where to write. If the two pointers are in the same spot
    and a write has to be performed, then the ring buffer needs to grow.
    '''
    def __init__(self):
        self._size = 0
        self._capacity = 2 # simulate manual memory management
        self._items = [None] * self._capacity
        self._read = 0
        self._write = 0

    def enqueue(self, item):
        if self.should_grow():
            self.grow()

        # Insert at write position
        self._items[self._write] = item

        # Increment write position
        self._write = (self._write + 1) % self._capacity

        # Increment size
        self._size += 1

    def dequeue(self):
        res = self._items[self._read]

        # Python shifts elements in list over automatically
        self._items[self._read] = None

        # Increment read pointer position
        self._read = (self._read + 1) % self._capacity

        # Decrement size
        self._size -= 1

        return res

    def size(self):
        return self._size

    def is_empty(self):
        return self._size == 0;

    def should_grow(self):
        return self._read == self._write and not self.is_empty()

    def grow(self):
        # allocate new empty spots
        new_capacity = self._capacity * 2
        delta_capacity = new_capacity - self._capacity
        new_empty_spots = [None] * delta_capacity

        # Copy over old items
        items_before_read = self._items[0:self._read]
        items_from_read_on = self._items[self._read:self._capacity]

        # Copy over old items to new array with read at beginning
        self._items = items_from_read_on + items_before_read + new_empty_spots
        self._read = 0

        # set write pointer at beg
        self._write = self._capacity

        # Update capacity to new capacity
        self._capacity = new_capacity
