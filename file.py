import os
# documentation, following the template
# comments
f = os.path.expanduser('//customer.txt')
def read_data():
    # read data from a file as one string into your program, return the string
    my_file = open('customer.txt')
    contents = my_file.read()
    my_file.close()
    print(contents)
    return contents

def bmi_calculate(contents):
    # data is read from the file in read_data()
    # return a dict in format: name:bmi
    customer_dict = {}
    for line in contents.split('\n'):
        print(line)
        # total += int(line)
        customer = line.split()
        for i in range(len(customer)):
            name = customer[0]
            w = float(customer[1])
            h = float(customer[2])
            bmi = 703 * w / h ** 2
            customer_dict[name] = round(bmi, 1)
    return  customer_dict

def write_data(customer_dict):
    # write calculated bmi into a ne file
    result_file = open('result.txt', 'w')
    for name, bmi in customer_dict.items:
        result_file.write(name+' '+ str(bmi)+"\n")
        result_file.close()

# testing block
if __name__ == '__main__':
    data = read_data()
    bmis = bmi_calculate(data)
    write_data(bmis)
    # testing if calculated data is saved into the file
    print('The result.txt content')
    result = open('results.txt')
    print(result.read())
    result.close()