class Student:
    grade = None
    height = None
    nice = None

    def __init__(self, grade: str, height: int, nice: bool):
        if grade not in ['U', '3', '4', '5']:
            raise Exception("")
        if not 111 < height < 211:
            raise Exception("")

        self.grade = grade
        self.height = height
        self.nice = nice


def perfect_hash(s: Student):
    grade_conv = {
        'U': 0,
        '3': 1,
        '4': 2,
        '5': 3
    }

    nice_conv = {
        True: 1,
        False: 0
    }

    h = 4 * hash(grade_conv[s.grade])
    h = 100 * h + hash(s.height)
    h = 2 * h + hash(nice_conv[s.nice])

    return h


if __name__ == "__main__":
    s = Student('3', 170, True)

    print(perfect_hash(s))
