from collections import Counter

s = input()
freq = Counter(s)

letters = sorted(freq)
result = []
n = len(s)

for _ in range(n):
    placed = False

    for ch in letters:

        if freq[ch] == 0:
            continue

        if result and result[-1] == ch:
            continue

        freq[ch] -= 1

        remaining = n - len(result) - 1

        # only 26 letters, so this is cheap
        max_freq = max(freq.values())

        if max_freq <= (remaining + 1) // 2:
            result.append(ch)
            placed = True
            break

        freq[ch] += 1

    if not placed:
        print(-1)
        exit()

print("".join(result))
