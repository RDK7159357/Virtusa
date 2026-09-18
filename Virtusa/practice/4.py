S=input()
M= int(input())
A=list(map(int,input().split()))
chars = list(S)
n=len(chars)
half = n//2
for i in A:
    if i==1:
        chars[0],chars[-1] = chars[-1],chars[0]
    elif i==2:
        chars=chars[half:]+chars[:half]
print("".join(chars))