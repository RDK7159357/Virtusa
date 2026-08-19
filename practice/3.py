def check(n):
    c=0
    while(n>0):
        if(n&1==1):
            c+=1
        n=n>>1
    return c
N=int(input())
M=int(input())
K=int(input())
arr=list(map(int,input().split()))
john = arr[N]
count=0
for i in range(N):
    diff = john^arr[i]
    if(check(diff)<=K):
        count+=1
print(count)