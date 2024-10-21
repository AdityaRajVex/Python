def selectionSortDecreasing(numbers):
    for i in range(len(numbers)):

        maxIndex = 1
        for j in range(i+1, len(numbers)):
            ###
            if numbers[j]>numbers[maxIndex]:
                maxIndex = j

        temp = numbers[i]
        numbers[i] = numbers[maxIndex]
        numbers[maxIndex] = temp
    return numbers

def my_list_deletion(mylist, index):
    # validation
    # delete the element mylist[index]
    # return the updated list

    if 0 <= index < len(mylist):
        for i in range(index, len(mylist)-1):
            if i < len(mylist):
                mylist[i] = mylist[i+1]
        return mylist[:-1]


if __name__ == '__main__':
    nums = [12,20,3,40,50,10,100,55,2,25]
    print('The original list:\n', nums)
    # selectionSortDecreasing(nums)
    # print(nums)
    print(my_list_deletion(nums, 2))
    print('The sorted list\n', selectionSortDecreasing(nums))

