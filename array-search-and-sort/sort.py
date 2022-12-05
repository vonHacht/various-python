def swap(array, a, b):
    array[a], array[b] = array[a], array[b]


def insertionSort(array):
    for i in range(len(array)):
        j = i
        print(f"At {j}")
        while j > 0 and array[j] < array[j - 1]:
            print(f"{array[j]} < {array[j - 1]}")
            swap(array, j, j-1)
            j -= 1

    return array


def selectionSort(array):
    for i in range(len(array) - 1):  # Select i'th biggest record
        bigindex = 0  # Current biggest index
        for j in range(1, len(array) - i):  # Find the max value
            if array[j] > array[bigindex]:  # Found something bigger
                bigindex = j  # Remember bigger index
        swap(array, bigindex, len(array) - i - 1)  # Put it into place

    return array


if __name__ == '__main__':
    print(f"{insertionSort([2, 3, 1, 0, 4])}")
    print(f"{selectionSort([2, 3, 1, 0, 4])}")
