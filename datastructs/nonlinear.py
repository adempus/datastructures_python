''' contains classes of data structures that order elements in a non-linear sequence'''
class BinaryNode(object):
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def isLeaf(self):
        return self.left is None and self.right is None

    def __str__(self):
        return f"\ndata: {self.data} \nL:{self.left.data} \nR:{self.right.data}"

    def __eq__(self, otherNode):
        if isinstance(otherNode, BinaryNode):
            return self.data == otherNode.data and self.left == otherNode.left and self.right == otherNode.right
        else:
            return False


ROOT = BinaryNode()

class BinaryTree(object):
    def __init__(self, initialData=None):
        self.__size = 0
        if initialData is not None:
            self.add(initialData)
            self.__increment()


    def add(self, data):
        if data:
            if ROOT.data is None:
                ROOT.data = data
            else:
                self.__add(data, ROOT)

    def __add(self, data, node):
        if node.data >= data:
            if node.left is None:
                node.left = BinaryNode(data)
                self.__increment()
            else:
                self.__add(data, node.left)
        elif node.data < data:
            if node.right is None:
                node.right = BinaryNode(data)
                self.__increment()
            else:
                self.__add(data, node.right)
        else:
            pass


    def remove(self, data):
        self.__remove(data, ROOT)

    def __remove(self, data, node):
        if node is None: return None
        if data < node.data:
            node.left = self.__remove(data, node.left)
        elif data > node.data:
            node.right = self.__remove(data, node.right)
        else:
            if node.isLeaf():
                self.__decrement()
                return None
            elif not node.isLeaf() and node.left is None:
                self.__decrement()
                return node.right
            elif not node.isLeaf() and node.right is None:
                self.__decrement()
                return node.left
            else:
                minVal = self.getMin(node.right)
                node.data = minVal
                node.right = self.__remove(minVal, node.right)
        return node


    def getMin(self, node=ROOT):
        if node is None:
            return None
        elif node.left is None:
            return node.data
        return self.getMin(node.left)


    def getMax(self, node=ROOT):
        if node is None:
            return None
        elif node.right is None:
            return node.data
        return self.getMax(node.right)


    def getPreorder(self):
        def preorderList(node=ROOT, result=list()):
            if node is not None:
                result.append(node.data)
                preorderList(node.left, result)
                preorderList(node.right, result)
                return result
        return preorderList(result=[])


    def getInorder(self):
        def inorderList(node=ROOT, result=list()):
            if node is not None:
                inorderList(node.left, result)
                result.append(node.data)
                inorderList(node.right, result)
                return result
        return inorderList(result=[])


    def getPostorder(self):
        def postList(node=ROOT, result=list()):
            if node is not None:
                postList(node.left, result)
                postList(node.right, result)
                result.append(node.data)
            return result
        return postList(result=[])


    def getRoot(self):
        return ROOT


    def __increment(self):
        self.__size += 1


    def __decrement(self):
        self.__size -= 1


    def size(self):
        return self.__size


    def __eq__(self, binTree):
        ''' :param binTree: a BinaryTree object
            :returns False if the specified binary tree is not identical to this one. True otherwise
        '''
        if len(binTree) != self.__size:
            return False
        else: return self.__isEq(ROOT, binTree.getRoot())


    def __isEq(self, node1, node2):
        if not node1 and not node2:
            return True
        if node1 and node2:
            if node1 != node2:
                return False
            if not self.__isEq(node1.left, node2.left):
                return False
            if not self.__isEq(node1.right, node2.right):
                return False
            return True
        return False


    def __len__(self):
        return self.size()