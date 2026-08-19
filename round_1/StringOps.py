def string_operations(S, M, A):
    chars = list(S)
    n = len(chars)
    half = n // 2

    for op in A:
        if op == 1:
            # Swap first and last character
            chars[0], chars[-1] = chars[-1], chars[0]
        elif op == 2:
            # Swap first half and second half
            chars = chars[half:] + chars[:half]

    return "".join(chars)


# Example Usage:
print(string_operations("abcdef", 2, [1, 2]))  # Output: "defabc"