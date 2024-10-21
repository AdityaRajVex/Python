from BinarySearchTree import BinarySearchTree
from Inventory import Inventory

def main():
    myTree = BinarySearchTree()
    inv1 = Inventory(1001, 1)
    inv2 = Inventory(100, 2)
    inv3 = Inventory(2005, 2)
    inv4 = Inventory(2005, 2)
    inv5 = Inventory(2005, 2)
    myTree.insert(inv1)