from d_ll import DoublyLinkedList


# Understand
# ==========
# Implement a ring-buffer (has limit)
# append -> adds element to the buffer
# get -> returns a list of all the elements in a dll in their given order
# the get shouldn't return `None` values in the list even if they are present in the ring buffer
# When the ring buffer is full and a new item is inserted
# the oldest element is overwritten with the newest element


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        """
        Adds an element to the ring buffer.
        """
        # if the cache is at capacity
        if self.storage.length == self.capacity:
            # Check if current is the tail
            if self.current is self.storage.tail:
                # if it is
                # change current to the head
                self.current = self.storage.head
            else:
                # Move to the next node
                self.current = self.current.next
            self.current.value = item
        # otherwise
        else:
            # add the item to the tail
            self.storage.add_to_tail(item)
            self.current = self.storage.tail

    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # get -> returns a list of all the elements in a dll in their given order
        # the get shouldn't return `None` values in the list even if they are present in the ring buffer
        # TODO: Your code here
        current = self.storage.head
        while current is not None:
            list_buffer_contents.append(current.value)
            current = current.next

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = [None] * capacity
        self.current = -1

    def append(self, item):
        self.current += 1
        if self.current == len(self.storage):
            self.current = 0
        self.storage[self.current] = item

    def get(self):
        return [i for i in self.storage if i is not None]


if __name__ == '__main__':
    buffer = RingBuffer(3)

    print(buffer.get())  # should return []

    buffer.append('a')
    buffer.append('b')
    buffer.append('c')

    print(buffer.get())   # should return ['a', 'b', 'c']

    # 'd' overwrites the oldest value in the ring buffer, which is 'a'
    buffer.append('d')

    print(buffer.get())  # should return ['d', 'b', 'c']

    buffer.append('e')
    buffer.append('f')

    print(buffer.get())   # should return ['d', 'e', 'f']
