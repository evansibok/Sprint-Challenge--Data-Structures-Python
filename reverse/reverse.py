class Node:
    def __init__(self, value=None, next_node=None):
        # the value at this linked list node
        self.value = value
        # reference to the next node in the list
        self.next_node = next_node

    def get_value(self):
        return self.value

    def get_next(self):
        return self.next_node

    def set_next(self, new_next):
        # set this node's next_node reference to the passed in node
        self.next_node = new_next


class LinkedList:
    def __init__(self):
        # reference to the head of the list
        self.head = None

    def add_to_head(self, value):
        node = Node(value)
        if self.head is not None:
            node.set_next(self.head)

        self.head = node

    def contains(self, value):
        if not self.head:
            return False
        # get a reference to the node we're currently at; update this as we
        # traverse the list
        current = self.head
        # check to see if we're at a valid node
        while current:
            # return True if the current value we're looking at matches our
            # target value
            if current.get_value() == value:
                return True
            # update our current node to the current node's next node
            current = current.get_next()
        # if we've gotten here, then the target node isn't in our list
        return False

    def reverse_list(self, node, prev):
        # You must use recursion for this solution

        # 1 -> 2 -> 3 -> 4
        # 4 -> 3 -> 2 -> 1
        # If node is empty or node's next is empty
        if node is None or node.get_next() is None:
            # return the node
            # --> if node is None, it will return None
            # --> if node's next is None, it will return the current node
            return node
        # Set the head node to be the recursive call of moving through the nodes
        self.head = self.reverse_list(node.get_next(), node)
        # Set the current next of the current node's next element to the current node
        # Same as pointing the current node's next element's next to the previous node
        node.get_next().set_next(node)
        # Point the current node's next to None
        node.next = None
        # Return the head node which will be the result of the
        # recursive call stack (the last held head node)
        return self.head
