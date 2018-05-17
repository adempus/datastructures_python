class Node(object):
    def __init__(self, data=None):
        self.__data = data
        self.__nextNode = None
        self.__prevNode = None

    def getData(self):
        ''' :returns the information contained in this node. '''
        return self.__data


    def getPrev(self):
        ''' :returns the node directly linked to the left of this one'''
        return self.__prevNode


    def getNext(self):
        ''' :returns the node directly linked to the right of this one. '''
        return self.__nextNode


    def setData(self, data):
        ''' data  :param - a piece of information to assign in this node. '''
        self.__data = data


    def setPrev(self, prevNode):
        '''nextNode  :param - a node to directly link to the left of this node. '''
        self.__prevNode = prevNode


    def setNext(self, nextNode):
        '''nextNode  :param - a node to directly link to the right of this node. '''
        self.__nextNode = nextNode

