s = input()
vowel = []
cons = []

for ch in s:
    if ch in "aeiou":
        vowel.append(ch)
    else:
        cons.append(ch)

result = ""
for i in range(len(vowel)):
    result += cons[i]
    result += vowel[i]

print(result)