def reduce_bill(n):
    b = list(bin(n)[2:])
    ans = float("inf")
    for i in range(0, len(b)):
        temp = b[:]
        if temp[i] == "0":
            temp[i] = "1"
        else:
            temp[i] = "0"
        num = int("".join(temp), 2)
        ans = min(ans, num)
    return ans


# Driver Code / Execution:
n = int(input())
print(reduce_bill(n))