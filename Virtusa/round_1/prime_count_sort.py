def prime_count(x):
    c = 0
    while x > 0:
        rem = x % 10
        if rem in [2, 3, 5, 7]:
            c += 1
        x = x // 10
    return c


def prime_sort(arr):
    arr.sort(key=lambda x: (prime_count(x), x))
    return arr


# Driver Code / Execution:
n = int(input())
arr = list(map(int, input().split()))
print(prime_sort(arr))