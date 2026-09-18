from collections import Counter

s = input()
d = Counter(s)
lst = list(d.items())
lst.sort(key=lambda x : -x[1])

res = ""
for key,value in lst:
    for i in range(value):
        res+=key

print(res) 
print(d)
print(lst)

# tree
# eetr
# Counter({'e': 2, 't': 1, 'r': 1})
# [('e', 2), ('t', 1), ('r', 1)]