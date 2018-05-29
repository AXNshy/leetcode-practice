def _softup(x, pos):
    lt = len(x)
    if pos >= lt:
        return
    left = 2 * pos + 1
    right = 2 * pos + 2
    smallest = None
    if isinstance(x[pos], tuple):
        if left < lt and x[left][0] < x[pos][0]:
            smallest = left
        else:
            smallest = pos
        if right < lt and x[right][0] < x[smallest][0]:
            smallest = right
    else:
        if left < lt and x[left] < x[pos]:
            smallest = left
        else:
            smallest = pos
        if right < lt and x[right] < x[smallest]:
            smallest = right
    if smallest != pos:
        temp = x[pos]
        x[pos] = x[smallest]
        x[smallest] = temp
        _softup(x, smallest)


def heapify(x):
    for i in reversed(range(len(x)//2)):
        _softup(x, i)


def pop(x):
    if not x:
        return None
    r = x[0]
    temp = x[-1]
    if r == temp:
        x.pop(0)
        return r[0], r[1]
    x[0] = temp
    x.pop(len(x) - 1)
    _softup(x, 0)
    return r[0], r[1]


def push(x, item):
    x.append(item)
    lt = len(x)
    smallest = lt
    while lt // 2 > 0:
        if x[(lt // 2)-1][0] > x[smallest-1][0]:
            temp = x[(lt // 2)-1]
            x[(lt // 2)-1] = x[smallest-1]
            x[smallest-1] = temp
            smallest = lt // 2
        else:
            break
