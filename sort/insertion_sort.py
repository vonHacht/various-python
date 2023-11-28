def swap(array, a, b):
    array[a], array[b] = array[a], array[b]


def insertion_sort(array):
    for i in range(len(array)):
        j = i
        print(f"At {j}")
        while j > 0 and array[j] < array[j - 1]:
            print(f"{array[j]} < {array[j - 1]}")
            swap(array, j, j - 1)
            j -= 1

    return array


if __name__ == '__main__':
    print(f"{insertion_sort([2, 3, 1, 0, 4])}")
