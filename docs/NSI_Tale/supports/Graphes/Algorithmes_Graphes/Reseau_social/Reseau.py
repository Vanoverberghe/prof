def inverser_l(f):
    l = []
    while f:
        e = f.pop()
        l.append(e)
        print(l)
    for i in l:
        f.append(i)
    return f