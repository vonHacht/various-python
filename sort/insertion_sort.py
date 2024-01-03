def swap(array, a, b):
    array[a], array[b] = array[b], array[a]


def insertion_sort(array):
    for i in range(len(array)):
        j = i
        print(array[j])
        while j > 0 and array[j] < array[j - 1]:
            swap(array, j, j - 1)
            j -= 1
        print(array)

    return array


if __name__ == '__main__':
    print(f"{insertion_sort([0, 3, 1, 0, 4])}")
