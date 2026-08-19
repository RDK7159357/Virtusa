s=input()
min_len = len(s)
for char in set(s):
    span = s.rfind(char) - s.find(char )+1
    min_len = min(min_len, span)
print(min_len)