from queue import Queue


class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def depth_first_for_each(self, cb):
        # Do for self
        cb(self.value)
        # Do for left
        if self.left:
            self.left.depth_first_for_each(cb)
        # Do for right
        if self.right:
            self.right.depth_first_for_each(cb)

    def breadth_first_for_each(self, cb):
        # Go through each level of the tree, on the current level
        # invoke the callback function with the value of each node, and
        # add the node's children to a Queue of open nodes.
        # Once the current depth is complete, the Queue will hold the nodes
        # from the next level. Repeat the process with those.

        # Define the open nodes queue
        open_nodes = Queue()
        open_nodes.enqueue(self)
        # Iterate over each node
        while open_nodes.len(): 
            # Invoke the callback for the current value
            current_node = open_nodes.dequeue()
            cb(current_node.value)
            # Queue-up the child nodes for the next depth level
            if current_node.left:
                open_nodes.enqueue(current_node.left)
            if current_node.right:
                open_nodes.enqueue(current_node.right)

    def insert(self, value):
        new_tree = BinarySearchTree(value)
        if (value < self.value):
            if not self.left:
                self.left = new_tree
            else:
                self.left.insert(value)
        elif value >= self.value:
            if not self.right:
                self.right = new_tree
            else:
                self.right.insert(value)

    def contains(self, target):
        if self.value == target:
            return True
        if self.left:
            if self.left.contains(target):
                return True
        if self.right:
            if self.right.contains(target):
                return True
        return False

    def get_max(self):
        if not self:
            return None
        max_value = self.value
        current = self
        while current:
            if current.value > max_value:
                max_value = current.value
            current = current.right
        return max_value
