def sequentialSearch(elements, e):
    for i in range(len(elements)):  # For each element
        if elements[i] == e:  # if we found it
            return i  # return this position
    return -1  # Otherwise, return -1


if __name__ == '__main__':
    print(f"{sequentialSearch('bananer', 'e')}")
