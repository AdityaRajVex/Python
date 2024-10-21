# linked list based queue
# front, rear

from Node import Node


class Queue():
    def __init__(self):
        self.front = None
        self.rear = None
        self.__length = 0

    def isEmpty(self):
        if not self.front:
            return True
        else:
            return False

    def enqueue(self, data):
        # append to the rear
        new_node = Node(data)
        # if the queue is empty
        if not self.front:
            self.front = new_node
            self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self.__length += 1

    def dequeue(self):
        # retrieve from the front
        if not self.front:
            # empty queue
            print('Empty queue')
            return None
        else:
            data = self.front.get_data()
            self.front  = self.front.next
            self.__length -= 1
            return data

    def peek(self):
        if self.front.isEmpty():
            return None
        return self.front.get_data()

    def getLength(self):
        return self.__length

if __name__ == '__main__':
    myQ = Queue()
    myQ.enqueue(5.0)
    myQ.enqueue(2.5)
    myQ.enqueue(10)
    print('The data in the queue:')
    while not myQ.isEmpty():
        print(myQ.dequeue(), end='->')
    print(f'\n{myQ.isEmpty()}')
