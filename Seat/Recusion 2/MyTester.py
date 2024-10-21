def main():
    # recursive message()
    message(3)


def message(times):
    if times > 0:
        print('Hello World!')
        message(times-1)


def message_loop(times):
    for i in range(times):
        print('Hello World!')


def factorial_loop(n):
    num = 0
    for x in range(n):
        num *= (x + 1)
        return num


def factorial(n):
    if n < 1:
        return 1
    else:
        return n*factorial(n-1)


if __name__ == '__main__':
    main()
