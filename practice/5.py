N=int(input())
A=list(map(int,input().split()))

total_or = 0
for num in A:
    total_or |= num

max_len=0
for i in range(N):
    for j in range(i,N):
        rem = A[:i]+A[j+1:]
        rem_or = 0

        for num in rem:
            rem_or |= num
        if rem_or == total_or:
            max_len = max(max_len,j-i+1)
print(max_len)