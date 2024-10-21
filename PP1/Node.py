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

if __name__ == '__main__':
    nums = [2,7,11,15]
    target = 9
    numMap = {}
    n = len(nums)

    # Build the hash table
    for i in range(n):
        numMap[nums[i]] = i
    print(range(n)
    print(numMap)

    # Find the complement
    for i in range(n):
        complement = target - nums[i]
        if complement in numMap and numMap[complement] != i:
            print([i, numMap[complement]])
