from collections import Counter

def lego(wall,n,blocks):
    if not blocks or not wall:
        return [-1]
    L = len(blocks[0])
    total = L*n
    wall_length = len(wall)

    if total>wall_length:
        return [-1]
    target = Counter(blocks)
    res=[]
    for i in range(wall_length-total+1):
        window = wall[i:i+total]
        words=[]
        for j in range(0,total,L):
            words.append(window[j:j+L])
        if Counter(words)==target:
            res.append(i)

    return res if res else [-1]
