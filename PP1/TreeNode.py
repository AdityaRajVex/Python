class TreeNode:
    def __init__(self, data):
        self.__data = data
        self.left = None
        self.right= None

    def get_data(self):
        return self.__data.calculate()

    def get_age(self):
        return self.__data.get_age()

    def __str__(self):
        return f'{self.__data}'


if __name__ == '__main__':
    node1 = TreeNode(10)
    print('the node is: ')
    print(node1)