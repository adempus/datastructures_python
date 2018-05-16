from DataStructure.Node import Node


'''Represents a data structure that stores values in uni or bi-directional succession.'''
class LinkedList(object):
    _head_node = Node()
    _tail_node = Node()


    ''' constructor 
        data           :param - a piece of information to store in this list.
        doubly_linked  :param - False indicates that nodes in this list are only traversed uni-directionally (start to end); 
                                 otherwise nodes can be bi-directionally traversed (end to start & vice-versa). 
    '''
    def __init__(self, data=0, is_doubly_linked=False):
        self.__size = int(0)
        self.__current_point = None


    def push_front(self, data):
        ''' data :param - a piece of information to add at the front of this list. '''
        if self._head_node.get_next() is None:
            self._head_node.set_next(Node(data))
            self._head_node.get_next().set_next(
                self._tail_node
            )
            self._increment()
        else:
            new_node = Node(data)
            new_node.set_next(self._head_node.get_next())
            self._head_node.set_next(new_node)
            self._increment()


    def push_back(self, data):
        ''' data :param - a piece of information to add to the back of this list. '''
        if self._tail_node.get_next() is None:
            new_node = Node(data)
            self._tail_node.set_next(new_node)
            if self._head_node is None and self.__size < 1:
                self._head_node.set_next(new_node)
            self._increment()
        else:
            new_node = Node(data)
            new_node.set_next(self._tail_node.get_next())
            self._tail_node.set_next(new_node)
            self._increment()


    def insert(self, data, item):
        ''' inserts data in front of an item located in this list.
            data :param - a piece of information to add in front of a specified item in this list.
            item :param - a piece of information in this list to insert data in front of. '''


    def remove(self, data):
        ''' removes a specified piece of information from this list, if it exists.
            data :param - a piece of information to remove from this list. '''


    def replace(self, data, item):
        ''' replaces item in this list with some specified data, if item exists.
            data :param - a piece of information to replace with some specified item in this list.
            item :param - a piece of information in this list to replace with some data. '''


    def _increment(self):
        ''' increases the size of this list when a node is added to it. '''
        self.__size = self.__size + 1


    def _decrement(self):
        ''' decreases the size of this list when a node is removed from it. '''
        self.__size = self.__size - 1



    def __len__(self):
        return self.__size


    class DoublyLinkedNode(Node):
        'Nodes in a linked-list can be either singly, or doubly linked. This class reps an instance of a doubly linked node.'
        def __init__(self, prev_node=None, data=None, next_node=None):
            Node.__init__(data, next_node)
            self.prev_node = prev_node

        def get_prev_node(self):
            return self.prev_node

        def set_prev_node(self, prev_node=None):
            self.prev_node = prev_node

