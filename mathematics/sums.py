def sum1():
    sum = 0
    for k in range(1, 101):
        sum = sum + 1.0 / k

    return sum


def sum2():
    sum = 0
    for k in range(1, 100000001):
        sum = sum + pow(1.0 / k, 2)

    return sum


if __name__ == "__main__":
    print(sum1())
    print(sum2())
