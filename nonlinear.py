''' contains classes of data structures that order elements in a non-linear sequence'''
from enum import Enum

class Node(object):
    class Position(Enum):
        left, right = range(2)

    def __init__(self, data):
        self._data = data
        self._parent = None
        self._leftChild = None
        self._rightChild = None
        self._position = None

    def setData(self, data):
        ''':param data - a piece of information to assign in this node'''
        self._data = data

    def getData(self):
        ''' :returns '''
        return self._data

    def setParent(self, parent):
        self._parent = parent

    def getParent(self):
        return self._parent

    def setLeftChild(self, leftChild):
        self._leftChild = leftChild

    def getLeftChild(self):
        return self._leftChild

    def setRightChild(self, rightChild):
        self._rightChild = rightChild

    def getRightChild(self):
        return self._rightChild

    def getPosition(self):
        return self._position

    def setPosition(self, position):
        self._position = position

    def __str__(self):
        return str(self._data)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self._data == other._data
        else:
            return self._data == other


class BinaryTree(object):
    def __init__(self):
        self._rootNode = None
        self._size = 0


    def insert(self, data):
        if self._rootNode is None:
            self._rootNode = Node(data)
        else:
            self._insert(self._rootNode, data)


    def _insert(self, node, data):
        if node.getData() >= data:
            if node.getLeftChild() is None:
                newChild = Node(data)
                newChild.setParent(node)
                newChild.setPosition(Node.Position.left)
                node.setLeftChild(newChild)
                self._increment()
            else:
                self._insert(node.getLeftChild(), data)
        elif node.getData() < data:
            if node.getRightChild() is None:
                newChild = Node(data)
                newChild.setParent(node)
                newChild.setPosition(Node.Position.right)
                node.setRightChild(newChild)
                self._increment()
            else:
                self._insert(node.getRightChild(), data)


    def getRoot(self):
        return self._rootNode


    def _increment(self):
        self._size += 1


    def _decrement(self):
        self._size -= 1

    def __eq__(self, binTree):
        ''' :param - an object of type BinaryTree
            :returns False if the specified binary tree is not identical to this one. True otherwise
        '''
        if len(binTree) != self._size:
            return False
        else:
            return self._isEqual(self._rootNode, binTree.getRoot())


    def _isEqual(self, node1, node2):
        if not node1 and not node2:
            return True
        if node1 and node2:
            if node1 != node2:
                return False
            if not self._isEqual(node1.getLeftChild(), node2.getLeftChild()):
                return False
            if not self._isEqual(node1.getRightChild(), node2.getRightChild()):
                return False
            return True
        return False

    def __len__(self):
        return self._size