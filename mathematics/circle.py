def lattice_points_within_circle(radius):
    count = 0
    m = -radius
    while m <= radius:
        n = -radius
        while n <= radius:
            if pow(m, 2) + pow(n, 2) <= pow(radius, 2):
                count = count + 1
            n += 1
        m += 1
    return count


if __name__ == "__main__":
    print(lattice_points_within_circle(100))
