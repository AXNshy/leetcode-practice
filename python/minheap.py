def _softup(x, pos):
    lt = len(x)
    left = 2 * pos
    right = 2 * pos + 1
    smallest = None
    if isinstance(x[pos], tuple):
        if left < lt and x[left][0] < x[pos][0]:
            smallest = pos
        else:
            smallest = left
        if right < lt and x[right][0] < x[smallest][0]:
            smallest = right
    else:
        if left < lt and x[left] < x[pos]:
            smallest = pos
        else:
            smallest = left
        if right < lt and x[right] < x[smallest]:
            smallest = right
    if smallest != pos:
        temp = x[pos]
        x[pos] = x[smallest]
        x[smallest] = temp
        _softup(x, smallest)


def heapify(x):
    for i in reversed(len(x)/2):
        if i == 0:
            return
        _softup(x, i + 1)


def pop(x):
    if not x:
        return None
    r = x[0]
    temp = x[-1]
    if r == temp:
        x.pop(0)
        return r.val, r
    x[0] = temp
    x.pop(-1)
    _softup(x, 1)
    return r.val, r


def push(x, item):
    x.append(item)
    lt = len(x)
    smallest = lt
    while lt // 2 > 0:
        if x[lt // 2][0] < x[smallest][0]:
            temp = x[lt // 2]
            x[lt // 2] = x[smallest]
            x[smallest] = temp
            smallest = lt // 2
        else:
            break