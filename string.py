from collections import Counter



s = "anagram"

count_s = Counter(s)



t="nagaram"

count_t = Counter(t)


for a,b in count_t.items():
    if count_s[a] != b:
        print(False)
        break
else:
    print(True)

print(sorted(s) == sorted(t)) #True
print(sorted(s)) #['a', 'a', 'a', 'g', 'm', 'n', 'r']

