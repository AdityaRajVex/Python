class TreeNode:
    def __init__(self, data):
        self.__data = data
        self.left = None
        self.right= None

    def get_data(self):
        return self.__data

    def __str__(self):
        return f'{self.__data}'


if __name__=='__main__':
    node1 = treeNode(10)
    print('the node is: ')
    print(node1)