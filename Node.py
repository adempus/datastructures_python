class Node(object):
    # was briefly dismayed at the absence of constructor chaining in python
    # weird how difficult it can be to move from a relatively complex, to simple language.
    def __init__(self, data=None):
        self.data = data
        self.next_node = None


    def get_data(self):
        return self.data


    def get_next(self):
        return self.next_node


    def set_data(self, data):
        self.data = data


    def set_next(self, next_node):
        self.next_node = next_node


