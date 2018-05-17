from DataStructure.Node import Node


'''Represents a data structure that stores values in uni or bi-directional succession.'''
class LinkedList(object):
    ''' constructor 
        data           :param - a piece of information to store in this list.
        doubly_linked  :param - False indicates that nodes in this list are only traversed uni-directionally (start to end); 
                                 otherwise nodes can be bi-directionally traversed (end to start & vice-versa). 
    '''
    def __init__(self, data=None, is_doubly_linked=False):
        self.__size = int(0)                        # number of nodes in the list
        self.__headNode = Node()                    # the initial link to a sequence of values
        self.__tailNode = Node()                    # a link pointing to the back of this list
        self.__currentPos = self.__headNode         # a marker to track precedence when iterating over nodes


    def pushFront(self, data):
        ''' data :param - a piece of information to add at the front of this list.
        '''
        if self.__headNode.getNext() is None:
            newNode = Node(data)
            self.__headNode.setNext(newNode)
            newNode.setNext(self.__tailNode)
            newNode.setPrev(self.__headNode)
            self.__tailNode.setPrev(newNode)
            self.__increment__()
        else:
            newNode = Node(data)
            newNode.setNext(self.__headNode.getNext())
            self.__headNode.setNext(newNode)
            newNode.setPrev(self.__headNode)
            self.__increment__()


    def pushBack(self, data):
        ''' data :param - a piece of information to add to the back of this list.
        '''
        if self.__headNode.getNext() is None:
            newNode = Node(data)
            self.__headNode.setNext(newNode)
            newNode.setNext(self.__tailNode)
            newNode.setPrev(self.__headNode)
            self.__tailNode.setPrev(newNode)
            self.__increment__()
        else:
            newNode = Node(data)
            lastNode = self.__tailNode.getPrev()
            newNode.setPrev(lastNode)
            lastNode.setNext(newNode)
            newNode.setNext(self.__tailNode)
            self.__tailNode.setPrev(newNode)
            self.__increment__()


    def insert(self, data, item):
        ''' inserts data in front of an item located in this list.
            data :param - a piece of information to add in front of a specified item in this list.
            item :param - a piece of information in this list to insert data in front of.
        '''


    def remove(self, data):
        ''' removes a specified piece of information from this list, if it exists.
            data :param - a piece of information to remove from this list.
        '''


    def replace(self, data, item):
        ''' replaces item in this list with some specified data, if item exists.
            data :param - a piece of information to replace with some specified item in this list.
            item :param - a piece of information in this list to replace with some data.
         '''


    def __increment__(self):
        ''' increases the size of this list when a node is added to it. '''
        self.__size = self.__size + 1


    def __decrement__(self):
        ''' decreases the size of this list when a node is removed from it. '''
        self.__size = self.__size - 1


    def __len__(self):
        return self.__size


    def __iter__(self):
        return self


    def __next__(self):
        if self.__currentPos.getNext() is self.__tailNode:
            self.__currentPos = self.__headNode
            raise StopIteration
        else:
            self.__currentPos = self.__currentPos.getNext()
            return self.__currentPos.getData()


    def getHeadNode(self):
        return self.__headNode


