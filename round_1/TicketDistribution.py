def check(num):#retuns the number of 1's in the binary representation of num
    c = 0
    while num > 0:
        if (num & 1) == 1:
            c += 1
        num = num >> 1
    return c



def count_matching_friends(N, M, K, ticket):
    john_ticket = ticket[N]
    count = 0
    for i in range(N):
        # Bitwise difference using XOR
        diff = ticket[i] ^ john_ticket
        if check(diff) <= K:
            count += 1
    return count


# Example Usage:
print(count_matching_friends(2, 4, 1, [3, 7, 2]))