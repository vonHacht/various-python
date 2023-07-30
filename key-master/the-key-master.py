def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quicksort(left) + middle + quicksort(right)


def escape(N: int, x: list[int]):
    if len(x) != N:
        raise Exception("Error ... some msg ...")

    keys = []
    dict = {}

    for num in range(0, len(x)):
        print(f"Needs key {x[num]} to collect {num}")
        if x[num] is None:
            keys.append(num)
        else:
            if x[num] in dict:
                dict[x[num]].append(num)
            else:
                dict[x[num]] = [num]

    print(dict)

    while len(keys) > 0:
        key = keys.pop(0)
        if key in dict:
            for k in dict[key]:
                keys.append(k)
            del dict[key]

    if len(dict) != 0:
        raise Exception("Error ... some msg ...")


if __name__ == "__main__":
    N = 6

    #    0, 1,    2, 3, 4
    # x = [4, None, 1, 3, 2, 1] => error
    x = [4, None, 1, 1, 2, 1]

    escape(N, x)
