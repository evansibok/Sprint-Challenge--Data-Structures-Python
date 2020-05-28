class BinarySearchTree:
    def __init__(self, value=None):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Initialize a node
        node = BinarySearchTree(value)
        # no root node
        # If no root node
        if self.value is None:
            # Insert the bst with the value passed in
            self.value = node.value
            return self.value

        # if there's a root node
        # check if the value is greater than or equal to the root node's value
        # if it is greater than
        if value >= self.value:
            # check if no right node exists
            # if right node is empty
            if self.right is None:
                # insert the bst to the right
                self.right = node
                return self.right.value
            # otherwise
            else:
                # call insert recursively on the right
                return self.right.insert(value)
        # if the value is less than or equal to the root node's value
        # if it is less than
        else:
            # check if no left node exists
            # if left node is empty
            if self.left is None:
                # insert the bst to the left
                self.left = node
                return self.left.value
            # otherwise
            else:
                # call insert recursively on the left
                return self.left.insert(value)

    def contains(self, target):
        # if target matches value
        if target == self.value:
            # return True
            return True

        #  # if root node is empty
        if self.value is None:
            # return False
            return False
        # If target is less than root's value
        elif target < self.value:
           # -> if left node is empty
            if self.left is None:
                # -> if it is
                # -> return False
                return False
            # if it isn't empty
            else:
                # call contains recursively on the left
                return self.left.contains(target)
        # otherwise
        # If target is greater than root's value
        elif target > self.value:
            # -> if right node is empty
            if self.right is None:
                # -> if it is
                # -> return False
                return False
            # if it isn't empty
            else:
                # call contains recursively on the right
                return self.right.contains(target)
