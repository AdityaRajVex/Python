from TreeNode import treeNode

class binaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        newNode = treeNode(data)
        if not self.root:
            #empty tree, the newNode becomes the root
            self.root = newNode
            print(data, end='->')
        else:
            tranverse_ptr = self.root
            while tranverse_ptr:
                # find the position for the newnode
                if data <= tranverse_ptr.get_data():
                    #go to its left side
                    if not tranverse_ptr.left: #does not have left child
                        tranverse_ptr.left = newNode
                        print(data, end='->')
                        break
                    else:
                        tranverse_ptr = tranverse_ptr.left
                else:
                    #go the right side
                    if not tranverse_ptr.right:
                        tranverse_ptr.right = newNode
                        print(data, end='->')
                        break
                    else:
                        tranverse_ptr = tranverse_ptr.right
    def display(self):
        if not self.root:
            print('This is an empty tree!')
        else:
            print('The tree is not empty:')
            self._display_node(self.root)
    def _display_node(self, node):
        if node:
            if node.left:
                self._display_node(node.left)
            print(node, end='->')
            if node.right:
                self._display_node(node.right)


if __name__ == '__main__':
    print('entered data: ')
    myTree = binaryTree()
    myTree.insert(10)
    myTree.insert(5)
    myTree.insert(12)
    myTree.insert(15)
    myTree.insert(3)
    myTree.insert(9)
    myTree.insert(20)
    myTree.insert(11)
    myTree.insert(4)
    print()
    print('The bst is: ')
    myTree.display()




