S=input()
res=0
n = len(S)
for start in range(n):
    curr_ind = start
    block_num = 1
    total_len = 0
    while True:
        block_len = block_num+1
        if curr_ind+block_len>n:
            break
        expected =""
        for i in range(block_len):
            expected += chr(ord("a")+i)
        actual = S[curr_ind:curr_ind+block_len]
        if expected != actual:
            break
        total_len += block_len
        curr_ind += block_len
        block_num += 1
    res = max(res, total_len)
print(res)