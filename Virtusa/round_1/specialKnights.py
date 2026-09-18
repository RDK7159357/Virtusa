def special_knights(arr):
    n = len(arr)
    count = 0
    for i in range(0, n):
        left = 0
        right = 0
        # count powerfull knights on the left
        for j in range(i):
            if arr[j] > arr[i]:
                left += 1
        # count powerfull knights on the right
        for j in range(i + 1, n):
            if arr[j] > arr[i]:
                right += 1
        if left > right:
            count += 1
    return count


# Driver Code / Execution:
n = int(input())
arr = list(map(int, input().split()))
print(special_knights(arr))