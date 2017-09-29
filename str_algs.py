def f(a):
    p = len(a)
    for i in range(p // 2):
        a[i], a[p - i - 1] = a[p - i - 1], a[i]

    return a


a = 'hello, world'
a = list(a)
print(''.join(f(a)))
