class ListNode:
    """
    This class holds the nodes for a doubly linked list.
    """

    def __init__(self, value=None, prev=None, next=None):
        """
        This instantiates the ListNode class with previous and next references.
        """
        self.value = value
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"Value: {self.value}, PrevNode: {self.prev}, NextNode: {self.next}"

    def insert_after(self, value):
        """Wrap the given value in a ListNode and insert it after this node. Note that this node could already have a next node it is point to."""
        # copy the current node's previous to a variable
        cur_node_next = self.next
        # set the current node's next to the new node
        self.next = ListNode(value, self, self.next)
        # if the current node has a next
        if cur_node_next:
            # set its next to the new node
            cur_node_next.next = self.next

    def insert_before(self, value):
        """Wrap the given value in a ListNode and insert it before this node. Note that this node could already have a previous node it is point to."""
        # copy the current node's previous to a variable
        cur_node_prev = self.prev
        # set the current node's prev to the new node
        self.prev = ListNode(value, self.prev, self)
        # if the current node has a previous
        if cur_node_prev:
            # set its next to the new node
            cur_node_prev.next = self.prev

    def delete(self):
        """Rearranges this ListNode's previous and next pointers accordingly, effectively deleting this ListNode."""
        # If this node has a next
        if self.next:
            # set the next's previous to point to this node's previous
            self.next.prev = self.prev

        # If this node has a prev
        if self.prev:
            # set the prev's next to point to this node's next
            self.prev.next = self.next


class DoublyLinkedList:
    """
    This class holds references and operations for a doubly lined linked list's head and tail nodes.
    """

    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __repr__(self):
        return f"Head: {self.head}, Tail: {self.tail}"

    def __len__(self):
        """
        Return the length of the list.
        """
        return self.length

    def delete(self, node):
        """Removes a node from the list and handles cases where the node was the head or the tail"""
        # Check if a list exists
        # if it doesn't, return 'No list exists!
        if not self.head:
            return "No list exists!"
        # otherwise
        # check if there's only one item on the list
        if node == self.head and node == self.tail:
            # if there is, delete the node by setting the pointer
            # to the head and tail to None
            self.head = None
            self.tail = None
        # if the node to be deleted is the head
        elif node == self.head:
            # set the current head's next as the current head
            self.head = self.head.next
            # call the delete method on the node
            node.delete()
        elif node == self.tail:
            # set the current tail's prev as the current tail
            self.tail = self.tail.prev
            # call the delete method on the node
            node.delete()
        else:
            # call the delete method on the node
            node.delete()
        # Don't forget to reduce the list's length
        self.length -= 1

    def add_to_head(self, value):
        """
        Wraps the given value in a ListNode and inserts it as the new head of the list, and also setting the old head node's previous pointer accordingly.
        """
        new_node = ListNode(value)
        # increment the length of the list
        self.length += 1
        # Check if list is empty
        # if it is
        if not self.head and not self.tail:
            # set the head and the tail to the new node
            self.head = new_node
            self.tail = new_node
            return self.head.value
        # otherwise
        else:
            # copy the current head to a temp
            temp = self.head
            # set the previous of the current head to the new node
            self.head.prev = new_node
            # set the new node as current head
            self.head = new_node
            # set the current head's next to the copy
            self.head.next = temp
            return self.head.value

    def remove_from_head(self):
        """
        Removes the List's current head node, making the current head's next, the new head. Returns the value of the removed node.
        """
        # set the current head's value to a temp
        value = self.head.value
        # remove the head node
        self.delete(self.head)
        # return the value of the removed node
        return value

    def add_to_tail(self, value):
        """
        Wraps the given value in a ListNode and inserts it as the new tail of the list, and also setting the old tail node's next pointer accordingly.
        """
        new_node = ListNode(value)
        # increment the length of the list
        self.length += 1
        # if no list exists
        # Check if list is empty
        # if it is
        if not self.head and not self.tail:
            # set the head and the tail to the new node
            self.head = new_node
            self.tail = new_node
            return self.head.value
        # otherwise
        else:
            # copy the current tail to a temp
            temp = self.tail
            # set the next of the current tail to the new node
            self.tail.next = new_node
            # set the new node as current tail
            self.tail = new_node
            # set the current tail's prev to the copy (old tail)
            self.tail.prev = temp
            return self.tail.value

    def remove_from_tail(self):
        """
        Removes the List's current tail node, making the current tail's prev, the new tail. Returns the value of the removed node.
        """
        # Set the value of the current tail to a temp
        value = self.tail.value
        # call the delete method on the tail
        self.delete(self.tail)
        # return the deleted value from temp
        return value

    def move_to_front(self, node):
        """
        Move a particular node to the front of the list, making it the head.
        """
        # Check if there's a list
        # if no list
        if not self.head and not self.tail:
            # return "No list."
            return "No list exists!"
        # otherwise
        value = node.value
        # if the list contains one element
        if node is self.head and node is self.tail:
            # return "There's only one item in the list!"
            return "There's only one item in the list!"
        # otherwise
        elif node is self.head:
            # if the node to be deleted is the head
            # remove the node
            return
        elif node is self.tail:
            self.remove_from_tail()
        else:
            node.delete()
            self.length -= 1
        self.add_to_head(value)

    def move_to_end(self, node):
        """
        Move a particular node to the end of the list, making it the tail.
        """
        # Check if there's a list
        # if no list
        if not self.head and not self.tail:
            # return "No list."
            return "No list exists!"
        # otherwise
        value = node.value
        # if the list contains one element
        if node is self.head and node is self.tail:
            # return "There's only one item in the list!"
            return "There's only one item in the list!"
        # otherwise
        elif node is self.head:
            # if the node to be deleted is the head
            # remove the node
            self.remove_from_head()
        elif node is self.tail:
            return
        else:
            node.delete()
            self.length -= 1
        self.add_to_tail(value)

    def get_max(self):
        """
        Traverse the linked list and return the highest value in the list.
        """

        # If there list is empty
        if not self.head:
            # return "List is empty!"
            return "List is empty!"

        # otherwise
        # Get the current head's value
        # and set it as the max value
        max_value = self.head.value
        # move through the list
        cur_node = self.head
        while cur_node:
            # compare the current max value with the current node's value
            # if the max value is less than the current node's value
            if max_value < cur_node.value:
                # set the current node's value as the new max value
                max_value = cur_node.value
            cur_node = cur_node.next
        return max_value
