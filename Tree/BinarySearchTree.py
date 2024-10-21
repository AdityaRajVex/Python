# binary search tree class: node right child's data > node data>= node left child'data
# use TreeNode class
# developer:
# version:
# data:

from TreeNode import TreeNode


class BinarySearchTree():
    def __init__(self):
        self.root = None #The pointer to the root node

    def insert(self, data):
        #wrap data into a tree node
        newNode = TreeNode(data)
        #find the proper position
        if not self.root: # empty bst, new node will be the root node
            self.root = newNode
        else:
            # traverse
            curr = self.root #traverse pointer
            while curr:
                if data <= curr.get_data():
                    #new node will be added in the left side of the current node
                    if not curr.left:
                        # current node's left child is empty, then the new node can fill into it
                        curr.left = newNode
                        break
                    else:
                        curr = curr.left #travese to the next level
                else: #new node will be added on the right side of the node
                    if not curr.right:
                        curr.right = newNode
                        break
                    else:
                        curr = curr.right

    def display(self):
        #display the tree
        self._print_bst_node(self.root) #private method
        print()

    def _print_bst_node(self, node):
        if not node:
            return None
        else:
            self._print_bst_node(node.left) # print the left side of the node
            print(node, end= ' ')
            self._print_bst_node(node.right)

    def search(self, key):
        curr = self.root
        while curr:
            if key == curr.get_data():
                return True
            elif key < curr.get_data():
                curr = curr.left
            else:
                curr = curr.right
        return False

    def search_recursive(self, key):
        curr = self.root
        return self._search_node(key, curr)

    def _search_node(self,key, node):
        if key == node.get_data():
            pass
        elif key < node.get_data():
            pass
        else:
            pass

    def remove(self, key):
        par = None
        cur = self.root
        while cur:
            if key == cur.get_data(): #the current node is the node to be removed
                if not cur.left and not cur.right: #type 1: leaf node
                    if not par: #current node is a leaf node and at same time, it is the root
                        #print(f'The last node {cur.get_data()} is removed  ')
                        self.root = None
                    elif par.left == cur:
                        par.left = None
                    else:
                        par.right =None
                    print(f'The leaf node {cur.get_data()} is removed  ')
                elif not cur.left: #current node has right child only
                    if not par:
                        self.root = cur.right
                    else:
                        if par.left == cur:
                            par.left = cur.right
                        else:
                            par.right = cur.right
                    print(f'The node {cur.get_data()} is removed  ')
                    cur = cur.right
                    #break
                elif not cur.right: #the node to be deleted has left child only
                    if not par:
                        self.root = cur.left
                    else:
                        if par.left == cur:
                            par.left = cur.left
                        else:
                            par.right = cur.left
                    print(f'The node {cur.get_data()} is removed  ')
                    cur = cur.left
                else: #The node to be deleted has two children
                    traveller = cur.right
                    while traveller.left: #find a positiono for cur.left
                        traveller = traveller.left
                    traveller.left = cur.left # find the new position for the left child of the node to be deleted
                    if par:
                        if par.right == cur:
                            par.right = cur.right
                        else:
                            par.left = cur.right
                    else: #par == None, which means the cur = self.root
                        #par = cur
                        #cur = cur.right
                        self.root = cur.right
                    print(f'The node {cur.get_data()} is removed  ')
                    cur = cur.right
                break
            elif key < cur.get_data(): # traverse the tree, to find the position of key
                par = cur
                cur = cur.left

            else:
                par = cur
                cur = cur.right

    def removeS1(self, key): ## given value 'key', search it in the tree, it is found, remove it from the tree (remove the links of that node)
        #check if it is the root to be removed
        if key == self.root.get_data():
            #remove the root
            if self.root.right:
                #self.root = self.root.right #new root
                #then find the position for the root.left
                travel = self.root.right
                while travel.left:
                    travel = travel.left
                travel.left = self.root.left
                print(f'Root node is removed!New root is root right: {self.root.right}')
                self.root = self.root.right #root is deleted

            else: #root.right is empty
                self.root = self.root.left
                print(f'The root node {self.root.get_data()} is removed!')
        elif key < self.root.get_data(): #the node to be deleted is not the root
            par = self.root
            cur = self.root.left
            while cur:
                if key == cur.get_data(): #node is found
                    #type 1: leaf node
                    if not cur.left and not cur.right:
                        #the parent.left or parent.right point to none
                        if par.left == cur:
                            par.left = None
                        else:
                            par.right = None
                        print(f'The leaf node {cur.get_data()} is removed!')
                    #Type 2: internal node to be deleted has right child only
                    elif not cur.left:
                        if par.left == cur:
                            par.left = cur.right
                        else:
                            par.right = cur.right
                        print(f'The leaf node {cur.get_data()} is removed!')
                    #Type 3: internal node to be deleted has left child only
                    elif not cur.right: #has left child only
                        if par.left == cur:
                            par.left = cur.left
                        else:
                            par.right = cur.left
                        print(f'The leaf node {cur.get_data()} is removed!')
                    #type 4 :internal node to be deleted has two children
                    else: #the node to be deleted has two children
                        travel = cur.right
                        while travel.left:
                            travel = travel.left
                        travel.left = cur.left
                        if par.right == cur: #current is the right child of its parent
                            par.right = cur.right
                        else:
                            par.left = cur.right
                        print(f'The node {cur.get_data()} is removed!')
                        cur = cur.right
                    break
                else: #cur is not the node to be deleted, go to next level
                    par = cur
                    if key < cur.get_data():
                        cur = cur.left
                    else:
                        cur = cur.right
        else: #search the right side of the root
            pass

    def _remove_node(self, key, cur, par):
        while cur:
            if key == cur.get_data():  # node is found
                # type 1: leaf node
                if not cur.left and not cur.right:
                    # the parent.left or parent.right point to none
                    if not par: #cur is the root
                        par = None
                    elif par.left == cur:
                        par.left = None
                    else:
                        par.right = None
                    print(f'The leaf node {cur.get_data()} is removed!')
                # Type 2: internal node to be deleted has right child only
                elif not cur.left:
                    if not par: #cur is the root
                        par = cur
                    elif par.left == cur:
                        par.left = cur.right
                    else:
                        par.right = cur.right
                    print(f'The leaf node {cur.get_data()} is removed!')
                # Type 3: internal node to be deleted has left child only
                elif not cur.right:  # has left child only
                    if not par:
                        par = cur
                    elif par.left == cur:
                        par.left = cur.left
                    else:
                        par.right = cur.left
                    print(f'The leaf node {cur.get_data()} is removed!')
                # type 4 :internal node to be deleted has two children
                else:  # the node to be deleted has two children
                    travel = cur.right
                    while travel.left:
                        travel = travel.left
                    travel.left = cur.left
                    if par.right == cur:  # current is the right child of its parent
                        par.right = cur.right
                    else:
                        par.left = cur.right
                    print(f'The node {cur.get_data()} is removed!')
                    cur = cur.right
                break
            else:  # cur is not the node to be deleted, go to next level
                par = cur
                if key < cur.get_data():
                    cur = cur.left
                else:
                    cur = cur.right


#testing
if __name__ == '__main__':
    myTree = BinarySearchTree()
    myTree.insert(500)
    myTree.insert(300)
    myTree.insert(800)
    myTree.insert(750)
    myTree.insert(150)
    myTree.insert(900)
    myTree.insert(850)
    myTree.insert(250)
    myTree.insert(950)
    print('Tree is created: ')
    myTree.display()
    #print(myTree.search(4))
    #print(myTree.search(12))
    print('Tree is updated: ')
    myTree.remove(300)
    myTree.display()




