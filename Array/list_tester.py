#
#
def my_append(numbers, value):
    # numbers[len(numbers)] = value
    pass

def my_delete(numbers, index):
    if index >= len(numbers):
        print('Out of the range')
    else:
        for i in range(index, len(numbers)):
            numbers[i] = numbers[i+1]
        numbers = numbers[:len(numbers)-1]
    return numbers

if __name__ == '__main__':
    numbers = [1, 11, 20]
    for i in range(len(numbers)):
        print('element ', i, ':', numbers[i])
    my_append(numbers, 2)
    #my_append(numbers, 50)
    print(numbers)