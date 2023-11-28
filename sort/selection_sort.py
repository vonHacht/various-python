def swap(array, a, b):
    array[a], array[b] = array[a], array[b]


def selection_sort(array):
    for i in range(len(array) - 1):  # Select i'th biggest record
        bigindex = 0  # Current biggest index
        for j in range(1, len(array) - i):  # Find the max value
            if array[j] > array[bigindex]:  # Found something bigger
                bigindex = j  # Remember bigger index
        swap(array, bigindex, len(array) - i - 1)  # Put it into place

    return array


if __name__ == '__main__':
    print(f"{selection_sort([2, 3, 1, 0, 4])}")
