class Node(object):
    # was briefly dismayed at the absence of constructor chaining in python
    # perplexing how difficult it can be to move from a relatively complex, to simple language.
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node


    def get_data(self):
        return self.data


    def get_next(self):
        return self.next_node


    def set_data(self, data=None):
        self.data = data


    def set_next(self, next_node=None):
        self.next_node = next_node


