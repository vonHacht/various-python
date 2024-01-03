class SimpleStack:  # FILO

    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        item = self.items[-1]
        del self.items[-1]
        return item


if __name__ == '__main__':
    queue = SimpleStack()
    queue.push(1)
    queue.push(2)
    queue.push(3)
    queue.push(4)

    print(queue.pop())
    print(queue.pop())
