import queue

if __name__ == '__main__':
    l = ["A", "B", "C", "D", "E", "F", "G", "H"]

    s = []
    q = queue.Queue()

    while len(l) > 0:
        s.append(l.pop(0))

    while len(s) > 0:
        q.put(s.pop())

    while not q.empty():
        x = q.get()
        y = q.get()
        s.append(y)
        s.append(x)

    while len(s) > 0:
        l.append(s.pop())

    print(l)
