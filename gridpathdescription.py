import sys

s = sys.stdin.readline().strip()

conv = {"U": -9, "D": 9, "R": 1, "L": -1, "?": 0}
path = [conv[ch] for ch in s]

START = 10          # 1 * 9 + 1
END = 64            # 7 * 9 + 1

visited = [1] * 81
for x in range(1, 8):
    for y in range(1, 8):
        visited[x * 9 + y] = 0

dist = [99] * 81
for x in range(1, 8):
    for y in range(1, 8):
        dist[x * 9 + y] = abs(x - 7) + abs(y - 1)


def solve(pos, step):
    if pos == END:
        return 1 if step == 48 else 0

    rem = 48 - step
    if rem == 0 or dist[pos] > rem:
        return 0

    visited[pos] = 1

    u = visited[pos - 9]
    d = visited[pos + 9]
    l = visited[pos - 1]
    r = visited[pos + 1]

    if (u and d and not l and not r) or (l and r and not u and not d):
        visited[pos] = 0
        return 0

    move = path[step]

    if move:
        nxt = pos + move
        if visited[nxt]:
            visited[pos] = 0
            return 0

    forced = -1
    forced_count = 0

    for n in (pos - 9, pos + 9, pos + 1, pos - 1):
        if (
            not visited[n]
            and n != END
            and visited[n - 9] + visited[n + 9] + visited[n - 1] + visited[n + 1] == 3
        ):
            forced = n
            forced_count += 1

    if forced_count > 1:
        visited[pos] = 0
        return 0

    ans = 0

    if move:
        if forced_count == 0 or nxt == forced:
            ans = solve(nxt, step + 1)
    elif forced_count == 1:
        ans = solve(forced, step + 1)
    else:
        for nxt in (pos - 9, pos + 9, pos + 1, pos - 1):
            if not visited[nxt]:
                ans += solve(nxt, step + 1)

    visited[pos] = 0
    return ans


print(solve(START, 0))
'''
key concepts:
flattening the 9x9 grid into a single array, that is cheaper, because we can use arithmetic instead of tuple unpacking
split pruning
forced move pruning: if there is a neighbouring cell with 3 blocked neighbours, with one of those three being the CURRENT square,
then take that cell instantly, because reaching it later is impossible
there can only be one square that is a dead-end, that is (7, 1), so if the number of those squares is more than 1, end immediately
if target is farther away than number of remaining moves, end immediately
'''
