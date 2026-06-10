from math import factorial
from collections import Counter
s = input()
n = len(s)
freq = Counter(s)
ans = factorial(n)
for i in freq.values():
    ans //= factorial(i)
print(ans)
def backtrack(path):
    if len(path) == n:
        print(path)
        return
    for ch in sorted(freq):
        if freq[ch] > 0:
            freq[ch] -= 1
            backtrack(path + ch)
            freq[ch] += 1
backtrack("")