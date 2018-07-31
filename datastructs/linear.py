''' contains classes of data structures that order elements in a linear sequence. These classes are LinkedList, Stack and Queue '''

''' represents a single element containing data that is uni-directionally linked to another Node '''
class Node(object):
    def __init__(self, data=None):
        self._data = data
        self._nextNode = None

    def getData(self):
        ''' :returns the information contained in this node. '''
        return self._data

    def setData(self, data):
        ''' :param data - a piece of information to assign in this node. '''
        self._data = data

    def getNext(self):
        ''' :returns the node directly linked to the right of this one. '''
        return self._nextNode

    def setNext(self, nextNode):
        ''' :param nextNode - a node to directly link to the right of this node. '''
        if isinstance(nextNode, DoublyLinkedNode):
            nextNode.setPrevious(self)
        self._nextNode = nextNode

    def __str__(self):
        ''' :returns a string representation of the data contained in this node.
        '''
        return str(self._data)

    def __eq__(self, node):
         ''' :param node - an object of type Node to compare its data with this node's data.
             :returns true if the data this node's data matches the data contained in the specified node.
         '''
         if isinstance(node, Node):
             return self._data == node.getData()
         else:
             return self._data == node


''' represents a single element containing data that is bi-directionally linked between two other Nodes '''
class DoublyLinkedNode(Node):
    def __init__(self, data=None):
        super().__init__(data)
        self._previousNode = None

    def getPrevious(self):
        ''' :returns the node directly linked to the left of this one.
        '''
        return self._previousNode

    def setPrevious(self, prevNode):
        ''' :param prevNode - a node to directly link to the left of this one.
        '''
        self._previousNode = prevNode


'''  Represents a data structure that stores values in uni or bi-directional succession.'''
class LinkedList(object):
    def __init__(self, doublyLinked=False):
        ''' :param doublyLinked - False indicates that nodes in this list are only traversed uni-directionally
            (start to end); otherwise nodes can be bi-directionally traversed (end to start & vice-versa).
        '''
        self._size = int(0)                  # number of nodes in the list
        self._headNode = Node()              # the initial link to a sequence of values
        self._tailNode = DoublyLinkedNode()  # a link pointing to the back of this list
        self._currentPos = self._headNode    # a marker to track precedence when iterating over nodes
        self._isDoublyLinked = doublyLinked


    def __initNode(self, data=None):
        if self._isDoublyLinked:
            return DoublyLinkedNode(data)
        else:
            return Node(data)


    def pushFront(self, data):
        ''' :param data - a piece of information to add at the front of this list.
        '''
        if self.isEmpty():
            newNode = self.__initNode(data)
            self._headNode.setNext(newNode)
            newNode.setNext(self._tailNode)
            self._increment()
        else:
            newNode = self.__initNode(data)
            newNode.setNext(self._headNode.getNext())
            self._headNode.setNext(newNode)
            self._increment()


    def pushBack(self, data):
        ''' :param data - a piece of information to add to the back of this list.
        '''
        if self.isEmpty():
            newNode = self.__initNode(data)
            self._headNode.setNext(newNode)
            newNode.setNext(self._tailNode)
            self._tailNode.setPrevious(newNode)
            self._increment()
        else:
            newNode = self.__initNode(data)
            lastNode = self._tailNode.getPrevious()
            lastNode.setNext(newNode)
            newNode.setNext(self._tailNode)
            self._increment()

    def insert(self, item, data):
        ''' inserts data behind an item located in this list.
            :param item - a piece of information already in this list to insert data behind.
            :param data - a piece of information to add behind the specified item in this list.
        '''
        if not self.isEmpty():
            current = self._headNode
            while current is not self._tailNode:
                if current == item:
                    newNode = self.__initNode(data)
                    newNode.setNext(current.getNext())
                    current.setNext(newNode)
                    self._increment()
                    break
                else:
                    current = current.getNext()


    def remove(self, data):
        ''' removes the first encounter of data specified, from this list if it exists.
            :param  data - a piece of information to remove from this list.
            :return the requested for removal
        '''
        if not self.isEmpty():
            current = self._headNode
            while current is not self._tailNode:
                if current.getNext().getData() == data:
                    temp = current.getNext()
                    current.setNext(temp.getNext())
                    self._decrement()
                    return temp
                else:
                    current = current.getNext()

    def replace(self, data, repData):
        ''' replaces item in this list with some specified data, if item exists.
            :param data - the piece of information existing in this list to be replaced.
            :param repData - the piece of information replacing whatever data is specified.
         '''
        if not self.isEmpty():
            curData = self._headNode.getNext()
            while curData is not self._tailNode:
                if curData == data:
                    curData.setData(repData)
                    break
                else:
                    curData = curData.getNext()

    def getNode(self, data):
        ''' :returns the node in this list containing the specified data.
        '''
        current = self._headNode.getNext()
        while current is not self._tailNode:
            if current == data:
                return current
            else:
                current = current.getNext()

    def getLast(self):
        return self._tailNode.getPrevious()

    def isEmpty(self):
        ''' :returns true if the head node of this list does not point to at least one other node; false otherwise.
        '''
        return (self._headNode.getNext() is None or self._headNode.getNext() is self._tailNode) and (self._size < 1)

    def _increment(self):
        ''' increases the size of this list when a node is added to it. '''
        self._size += 1

    def _decrement(self):
        ''' decreases the size of this list when a node is removed from it. '''
        self._size -= 1

    def __len__(self):
        ''' :returns the number of nodes in this list'''
        return self._size

    def __iter__(self):
        return self

    def __next__(self):
        ''' traverses over the nodes in this list from left to right. '''
        if self._currentPos.getNext() is not self._tailNode:
            self._currentPos = self._currentPos.getNext()
            return self._currentPos
        else:
            self._currentPos = self._headNode
            raise StopIteration

    def __str__(self):
        string = "["
        for n in self:
            string+=str(n.getData())+', ' \
                                     ''
        string += ']'
        return string


'''Represents a contiguous structure that places elements in last-in first-out (LIFO) order'''
class Stack(object):
    def __init__(self):
        self._backingList = LinkedList()     # this stack is backed by a linked list
        self._recentPush = None              # for tracking the most recent push; makes for easy popping off the stack.

    def push(self, data):
        ''' :param data - a piece of information to pe pushed onto the front of this stack. '''
        self._backingList.pushFront(data)
        self._recentPush = data

    def pop(self):
        ''' :returns the top/front most element from this stack
        '''
        removedNode = self._backingList.remove(self._recentPush)
        self._recentPush = removedNode.getNext()
        return removedNode

    def getTop(self):
        ''' :returns the top node of this stack without removing it.
        '''
        return self._recentPush

    def __str__(self):
        stackStr = "["
        for node in self._backingList:
            stackStr += str(node)+", "
        return stackStr[0:(len(stackStr)-2)]+"]"

    def __len__(self):
        return len(self._backingList)


''' Represents a contiguous structure that places elements in first-in first-out (FIFO) order. '''
# TODO: Test the Queue class methods enqueue & dequeue
class Queue(object):
    def __init__(self):
        self._backingList = LinkedList()
        self._recentPush = None

    def enqueue(self, data):
        if len(self) < 1:
            self._backingList.pushBack(data)
            self._recentPush = self._backingList.getNode(data)
        else:
            self._backingList.pushBack(data)

    def dequeue(self):
        if len(self) > 1:
            nextTop = self._recentPush.getNext()
            self._backingList.remove(self._recentPush)
            self._recentPush = nextTop

    def __len__(self):
        return len(self._backingList)
