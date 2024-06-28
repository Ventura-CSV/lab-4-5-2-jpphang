import random


def main():
    total = 0
    numbers = []

    while total <= 100:
        ran_num = random.randint(1, 100)
        numbers.append(ran_num)
        total += ran_num

    print(f'The random values are {numbers}')
    print(f'The total is {total}')


    return numbers, total


if __name__ == '__main__':
    main()
