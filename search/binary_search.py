def binarySearch(elements, e):
    # needs to be sorted
    elements = ''.join(sorted(elements))

    low = 0
    high = len(elements) - 1
    while low <= high:  # Stop when low and high meet
        mid = (low + high) // 2  # Check middle of subarray
        print(f"|{low}| ... |{mid}| ... |{high}|")
        if elements[mid] < e:
            low = mid + 1  # In right half
        elif elements[mid] > e:
            high = mid - 1  # In left half
        else:
            return mid  # Found it
    return -1  # Search value not in array


if __name__ == '__main__':
    print(
        f"{binarySearch('Today is the day Ill finally know what brick tastes like.', 'o')}"
    )
