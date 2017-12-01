# BINARY TREE
# Author: Tom Smoker
# Date: 30/11/17

"""
Create a basic implementation of a binary tree in Python, for use in proofs
"""

# Create a class for each node in the tree
class Node:

    def __init__(self, key, val, left = None, right = None, parent = None):

        self.key        = key
        self.value      = val
        self.left_child  = left
        self.right_child = right
        self.parent     = parent

    def hasLeftChild(self):
        return self.left_child

    def hasRightChild(self):
        return self.right_child

    def isLeftChild(self):
        return self.parent and self.parent.left_child == self

    def isRightChild(self):
        return self.parent and self.parent.right_child == self

    def isRoot(self):
        return self.parent is None

    def isLeaf(self):
        return self.left_child is None or self.right_child is None

    def hasChildren(self):
        return self.left_child or  self.right_child

    def hasBothChildren(self):
        return self.left_child and self.right_child

    def replaceNodeData(self, key, val, left_child, right_child):

        self.key        = key
        self.value      = value
        self.left_child  = left_child
        self.right_child = right_child

        if self.hasLeftChild():
            self.left_child.parent = self

        if self.hasRightChild():
            self.right_child.parent = self

# Create the BST class
class BinarySearchTree:

    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

        # Create setter method to set nodes in the tree
        def set(self, key, val):

            if self.root:
                self._set(key, val, self.root)
            else:
                self.root = Node(key, val)

            self.size = self.size + 1

    # Helper set method for the recursive call
    def _set(self, key, val, current_node):

        if key < current_node.key:
            if current_node.hasLeftChild():
                self._set(key, val, current_node.leftChild)
            else:
                current_node.left_child = Node(key, val, parent = current_node)
        else:
            if current_node.hasRightChild():
                self._set(key, val, current_node.right_child)
            else:
                current_node.right_child = Node(key, val, parent = current_node)

    # Overloading the setitem method e.g. myTree['amount'] = 100
    def __setitem__(self, key, val):
        self.set(key, val)

    # Create getter method to get nodes from the tree
    def get(self, key):

        if self.root:
            desired_node = self.+get(key, self.root)

            if result:
                return result.value
            else:
                return None
        else:
            return None

    #Helper get method for the recursive call
    def _get(self, key, current_node):

        if current_node is None:
            return None
        elif current_node.key == key:
            return current_node
        elif key < current_node.key:
            return self._get(key, current_node.left_child)
        else:
            return self._get(key, current_node.right_child)

    # Overloading the getitem method e.g. balance = myTree['amount']
    def __getitem__(self, key):
        return self.get(key)

    # Check if a tree contains a node
    def __contains__(self, key):

        if self._get(key, self.root):
            return True
        else:
            return False

    # Delete a node from the tree
    def delete(self, key):

        if self.size < 1:
            raise KeyError("Tree does not contain this key")

        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = self.size - 1

        else:

            node_to_remove = self._get(key, self.root)

            if node_to_remove:
                self.remove(node_to_remove)
                self.size = self.size - 1
            else:
                raise KeyError("Tree does not contain this key")

    #Overload the __delitem__method
    def __delitem__(self, key):
        self.delete(key)

    #Method to clean up the children of deleted nodes
    def spliceOut(self):

        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.hasChildren():
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.isLeftChild():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    #Method to find the successor of the deleted node
    def findSuccessor(self):

        successor = None

        if self.hasRightChild():
            successor = self.right_child.findMin()
        else:
            if self.parent:
                if self.isLeftChild():
                    successor = self.parent
                else:
                    self.parent.right_child = None
                    successor = self.parent.findSuccessor()
                    self.parent.right_child = self

        return successor

    # Method to find the minimum node
    def findMin(self):

        current = self

        while current.hasLeftChild():
            current = current.left_child

        return current

    # Method to find the maximum node
    def findMax(self):

        current = self

        while current.hasRightChild():
            current = current.right_child

        return current
