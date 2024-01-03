class SimpleQueue:  # FIFO

    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        item = self.items[0]
        del self.items[0]
        return item


if __name__ == '__main__':
    queue = SimpleQueue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)

    print(queue.dequeue())
    print(queue.dequeue())
