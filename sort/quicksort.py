def quicksort(arr):
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]

    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    print(f"===============\n"
          f"pivot: {pivot}\n"
          f"{left} {middle} {right}\n"
          f"===============")

    return quicksort(left) + middle + quicksort(right)


if __name__ == "__main__":
    # print("A" < "B")
    # print("B" < "C")
    # print("C" < "D")

    # arr = ["E", "C", "B", "F", "G", "A", "D"]
    arr = [15, 74, 63, 51, 32, 48, 89, 91, 27]

    print(quicksort(arr))
