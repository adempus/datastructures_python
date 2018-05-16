class Node(object):
    # was briefly dismayed at the absence of constructor chaining in python
    # weird how difficult it can be to move from a relatively complex, to simple language.
    def __init__(self, data=None):
        self.__data = data
        self.__next_node = None
        self.__prev_node = None


    def get_data(self):
        return self.__data


    def get_next(self):
        return self.__next_node


    def set_data(self, data):
        self.__data = data


    def set_next(self, next_node):
        self.__next_node = next_node


    def get_prev(self):
        return self.__prev_node


    def set_prev(self, prev_node):
        self.__prev_node = prev_node
