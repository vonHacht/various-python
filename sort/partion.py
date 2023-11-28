def partion(arr, low, high):
    pivot = arr[low]

    i = low + 1
    j = high

    while i <= j:
        if arr[i] < pivot:
            i += 1
        elif arr[j] > pivot:
            j -= 1
        else:
            arr[i] = arr[j]
            i += 1
            j -= 1

    arr[low] = arr[j]
    return j


if __name__ == "__main__":
    print(partion([1, 2, 3, 4, 5], 0, 4))
