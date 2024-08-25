def counter(lst):
    ret = {}
    for n in lst:
        if n in ret:
            ret[n] += 1
        else:
            ret[n] = 1
    return (ret)

def solution(a, b, c, d):
    c = counter([a, b, c, d])
    l = len(c)
    print(c, l)
    
    keys = list(c.keys())
    vals = list(c.values())
    print(keys, vals)
    
    if l == 1:
        return (1111 * keys[0])
    elif l == 2:
        if vals[0] == vals[1]:
            return ((keys[0] + keys[1]) * abs(keys[0] - keys[1]))
        else:
            i = vals.index(3)
            other = vals.index(1)
            return ((keys[i] * 10 + keys[other]) ** 2)
    elif l == 3:
        i = vals.index(2)
        others = list(set([0, 1, 2]) - set([i]))
        return (keys[others[0]] * keys[others[1]])
    else:
        return (min(keys))