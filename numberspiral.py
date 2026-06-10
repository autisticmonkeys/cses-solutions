t = int(input())

for _ in range(t):
    y, x = map(int, input().split())
    r = y - 1
    c = x - 1
    k = max(r, c)
    if k % 2 == 0:
        if r <= c:
            val = (k + 1) ** 2 - r
        else:
            val = k * k + c + 1
    else:
        if r <= c:
            val = k * k + r + 1
        else:
            val = (k + 1) ** 2 - c
    print(val)
