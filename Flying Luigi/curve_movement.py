def mathematics_type_b(t, a, b, c, d):
    mx = ((-t ** 3 + 2 * t ** 2 - t) * a[0] + (3 * t ** 3 - 5 * t ** 2 + 2) * b[0] + (-3 * t ** 3 + 4 * t ** 2 + t) *
          c[0] + (t ** 3 - t ** 2) * d[0]) / 2
    my = ((-t ** 3 + 2 * t ** 2 - t) * a[1] + (3 * t ** 3 - 5 * t ** 2 + 2) * b[1] + (-3 * t ** 3 + 4 * t ** 2 + t) *
          c[1] + (t ** 3 - t ** 2) * d[1]) / 2
    return mx, my