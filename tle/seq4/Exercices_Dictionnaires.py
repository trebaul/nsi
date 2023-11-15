def tabToDict(t):
    d = {}
    for i in range(0, len(t), 2):
        d[t[i]] = t[i+1]
    return d

def dictToTab(d):
    l = []
    for c in d.keys():
        l.append(c)
        l.append(d[c])
    return l

