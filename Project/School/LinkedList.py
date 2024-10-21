# This is the linked list class, it is composed by Nodes

from Node import Node


class LinkedList:
    def __init__(self):
        self.head = None  # new created linked list is empty
        self.tail = None  # empty linkedlist

    def append(self, data):
        # wrap up data into a node
        new_node = Node(data)
        if self.head:  # not empty list
            # the self.head is not None
            # the linked list has nodes already
            self.tail.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def display(self):
        if self.head:
            # not empty list
            current = self.head  # a traverse pointer
            while current:
                print(current, end='->')
                current = current.next  # traverse to the next node
        else:
            print('The linked list is empty!')

    def search(self, value):
        # if any node's data equals the value, then return True, otherwise, return False
        current = self.head
        while current:
            if current.get_data() == value:
                return True
            else:
                current = current.next
        return False

    def search2(self, key):
        return self._recursiveSearch(key, self.head)

    def _recursiveSearch(self, key, node):
        if not node:
            return False
        elif node.get_data() == key:
                return True
        else:
            return self._recursiveSearch(key, node.next)

    def delete(self, value):
        # current = None
        previous = None
        if self.head:
            if self.head.get_data() == value:
                self.head = self.head.next
            else:
                current = self.head
                while current:
                    if current.get_data() == value:  # the current node should be removed from the linkedlist

                        previous.next = current.next
                        if current == self.tail:
                            self.tail = previous
                        print('It is deleted!')
                        return True
                    else:
                        previous = current
                        current = current.next

                return False

        else:
            print('This is an empty list!')

    def insert(self, value):
        # create an ascending linkedlist
        newNode = Node(value)

        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            if self.head.get_data() > value:
                # new node will be the head node
                newNode.next = self.head
                self.head = newNode

            elif self.tail.get_data() < value:
                # new node will be the tail
                self.tail.next = newNode
                self.tail = newNode

            else:
                current = self.head  # traverse pointer
                # find the proper position to insert this new node
                while current.get_data() < value and current.next and current.next.get_data() < value:
                    current = current.next
                # position is foundx
                newNode.next = current.next
                current.next = newNode

    def sort(self, choice=0):
        # traverse the linked list 
        if choice == 0:
            # ascending
            pass
        else:
            # descending
            pass

    def __str__(self):
        return f'{self.display()}'
# testing
if __name__ == '__main__':
    myLinkedList = LinkedList()
    # myLinkedList.display()
    myLinkedList.insert(2.5)
    # myLinkedList.display()
    myLinkedList.insert(9.5)
    myLinkedList.insert(6.5)
    myLinkedList.insert(15.0)
    myLinkedList.display()
    print(myLinkedList.search(15.0))
    print(myLinkedList.search(10.0))
