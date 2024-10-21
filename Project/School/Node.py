# this is the class of Node, it is used to build up the linked lists

class Node():
    def __init__(self, data):
        self.__data = data
        self.next = None # by default, a new node

    def __str__(self):
        # display the data of the node
        return f'{self.__data}'

    def get_data(self):
        return self.__data
