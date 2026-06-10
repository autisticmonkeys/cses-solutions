n = int(input())
if n * (n + 1) % 4 == 0:
    print("YES")
    if n % 4 == 0:
        k = n // 4
        first = range(1, k + 1)
        last = range(n - k + 1, n + 1)
        middle = range(k + 1, n - k + 1)
        print(n // 2)
        print(*first, *last)
        print(n // 2)
        print(*middle)
    else:
        k = (n + 1) // 4
        first = range(1, k)
        last = range(n - k + 1, n + 1)
        middle = range(k, n - k + 1)
        print((n // 2) + 1)
        print(*middle)
        print(n // 2)
        print(*first, *last)
else:
    print("NO")
