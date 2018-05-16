from DataStructure.Node import Node


'''Represents a data structure that stores values in uni or bi-directional succession.'''
class LinkedList(object):
    ''' constructor 
        data           :param - a piece of information to store in this list.
        doubly_linked  :param - False indicates that nodes in this list are only traversed uni-directionally (start to end); 
                                 otherwise nodes can be bi-directionally traversed (end to start & vice-versa). 
    '''
    def __init__(self, data=None, is_doubly_linked=False):
        self.__size = int(0)
        self.__head_node = Node()
        self.__tail_node = Node()
        self.__current_point = Node()


    def push_front(self, data):
        ''' data :param - a piece of information to add at the front of this list.
        '''
        if self.__head_node.get_next() is None:
            new_node = Node(data)
            self.__head_node.set_next(new_node)
            new_node.set_next(self.__tail_node)
            self.__tail_node.set_prev(new_node)
            self.__increment__()
        else:
            new_node = Node(data)
            new_node.set_next(self.__head_node.get_next())
            self.__head_node.set_next(new_node)
            self.__increment__()


        # if self.__head_node.get_next() is None:
        #     self.__head_node.set_next(Node(data))
        #     self.__head_node.get_next().set_next(
        #         self.__tail_node
        #     )
        #     self.__increment__()
        # else:
        #     new_node = Node(data)
        #     new_node.set_next(self.__head_node.get_next())
        #     self.__head_node.set_next(new_node)
        #     self.__increment__()


    def push_back(self, data):
        ''' data :param - a piece of information to add to the back of this list.
        '''
        if self.__head_node.get_next() is None:
            new_node = Node(data)
            self.__head_node.set_next(new_node)
            new_node.set_next(self.__tail_node)
            self.__tail_node.set_prev(new_node)
            self.__increment__()
        else:
            new_node = Node(data)
            self.__tail_node.get_prev().set_next(new_node)
            new_node.set_next(self.__tail_node)
            self.__tail_node.set_prev(new_node)
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


    def get_head_node(self):
        return self.__head_node


