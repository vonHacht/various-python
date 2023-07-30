import timeit


class DynamicArray:
    def __init__(self, amortized=False):
        self.size = 0
        self.amortized = amortized
        self.internal = [None] * 10

    def add_last(self, x):
        if self.size >= len(self.internal):
            self.resize()
        self.internal[self.size] = x
        self.size += 1

    def resize(self):
        if self.amortized:
            new_capacity = self.size * 2
        else:
            new_capacity = self.size + 100

        old_internal = self.internal
        self.internal = [None] * new_capacity
        for k in range(self.size):
            self.internal[k] = old_internal[k]


def run_comparison():
    num_operations = 100000  # Number of addLast operations to perform

    # Non-amortized strategy: Doubling size increase
    dynamic_array_non_amortized = DynamicArray()
    time_non_amortized = timeit.timeit(lambda: [dynamic_array_non_amortized.add_last(i) for i in range(num_operations)],
                                   number=1)

    # Amortized strategy: Constant size increase
    dynamic_array_amortized = DynamicArray(True)
    time_amortized = timeit.timeit(lambda: [dynamic_array_amortized.add_last(i) for i in range(num_operations)],
                                       number=1)

    print(f"Non-amortized time: {time_non_amortized:.6f} seconds")
    print(f"Amortized time: {time_amortized:.6f} seconds")


if __name__ == "__main__":
    run_comparison()
