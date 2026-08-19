def special_index(n, A):
    for i in range(n):
        left_xor = 0
        for j in range(0, i + 1):
            left_xor ^= A[j]

        right_xor = 0
        for j in range(i + 1, n):
            right_xor ^= A[j]

        if left_xor > right_xor:
            return i
    return -1


# Example Usage:
print(special_index(4, [4, 2, 1, 3]))