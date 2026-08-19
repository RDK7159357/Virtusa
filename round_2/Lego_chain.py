from collections import Counter


def find_lego_chains(wall, n, blocks):
    if not blocks or not wall:
        return [-1]

    L = len(blocks[0])
    total = n * L
    wall_len = len(wall)

    if total > wall_len:
        return [-1]

    target = Counter(blocks)
    result = []

    for i in range(wall_len - total + 1):
        window = wall[i : i + total]

        words = []
        for j in range(0, total, L):
            words.append(window[j : j + L])

        if Counter(words) == target:
            result.append(i)

    return result if result else [-1]

print(find_lego_chains("barfoothefoobarman", 2, ["foo", "bar"]))