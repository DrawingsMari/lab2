def f(a):
    p = None
    for i in a:
        if p is None or p < i:
            p = i
    return p


def sr(a):
    p = 0
    s = 0
    for i in a:
        p = p + 1
        s = s + i
    r = s / p
    return r


def sr2(a):
    return sum(a) / len(a)


a = [-2, 4, 7, 10, -190, 5, 0, 23, 7]
print(f(a))

print(sr(a))
print(sr2(a))
