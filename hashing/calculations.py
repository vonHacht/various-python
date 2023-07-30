from math import factorial, pow


class Person:
    def __init__(self, first, last):
        self.firstName = first
        self.lastName = last

    def __hash__(self):
        # Note: The function ``hash(x)`` calls ``x.__hash__()``
        return hash(self.firstName) + hash(self.lastName)


def binning(number, hash_table_size=100, key_range=(0, 9999)):
    if number > key_range[1]:
        raise ValueError(f"{number > key_range[1]}")

    return number / hash_table_size


def simpleModHashFunction(number, hash_table_size):
    return number % hash_table_size


def hashStringImproved(string, hash_table_size):
    sum = 0
    for c in string:
        sum = 31 * sum + ord(c)
    return sum % hash_table_size


def hashString(string, hash_table_size):
    sum = 0
    for c in string:
        sum += ord(c)
    return sum % hash_table_size


def collision(table_size, records):
    if table_size < records:
        raise ValueError(f"{table_size} < {records}")

    return 1 - factorial(table_size) / (factorial(table_size - records) * pow(table_size, records))


def mid_square_hash(key, table_size):
    # Square the key and convert it to a string
    square = str(key * key)

    # Extract the middle digits (or characters) of the squared value
    mid_index = len(square) // 2
    mid_digits = square[mid_index - 1:mid_index + 1]

    # Convert the middle digits to an integer and compute the hash value
    hash_val = int(mid_digits) % table_size

    return hash_val


if __name__ == '__main__':
    print(f"{collision(23, 7) * 100} %")
    print(f"{hashString('hello', 101)}")
    print(f"{hashStringImproved('hello', 101)}")
    print(f"{binning(3600)}")
    print(f"{hashString('hbrc1vbqo', 101)}")
    print(f"{mid_square_hash(3465, 100)}")
