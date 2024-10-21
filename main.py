import random
def get_even_values(numbers=[]):
    even_values = []
    for i in numbers:
        if i % 2 == 0:
            even_values.append(i)
    return even_values


def get_doubled(numbers=[]):
    for i in numbers:
        numbers[i] = numbers[i] * 2


def create_list_v2(size, number_list=[]):
    for i in range(size):
        value = random.randint(0, 100)
        number_list.append(value)