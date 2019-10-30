
s = []


def sa():
    p1 = (100, 600)
    p2 = (200, 25)

    x1, y1 = p1[0], p1[1]
    x2, y2 = p2[0], p2[1]
    a = (y2-y1) / (x2 - x1)
    b = y1 - x1 * a
    for x in range(x1, x2+1, 1):
        y = a * x + b
        s.append((x, y))


sa()

