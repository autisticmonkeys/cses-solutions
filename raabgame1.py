"""
if a + b > n, then return NO
if only one of a and b is 0, then return NO
if both a and b are 0, then return YES, the solution will be same numbers for both every round
for cases where a, b > 0, if a + b = n, then return YES
in this case, the solution will be 1 to n for the first player, and the last b numbers in the beginning for the second player, followed by 1 to n-b
for cases where a, b > 0, if a + b < n, then return YES
in this case, the solution will be 1 to n for the first player, then the first n - (a + b) numbers for the second player, then the last b numbers, followed by the remaining numbers for the second player
all this is for cases with a >= b, if b > a, then we can just swap the players and apply the same logic
"""

t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    if a + b > n:
        print("NO")
        continue
    if (a == 0 and b > 0) or (b == 0 and a > 0):
        print("NO")
        continue
    if a == 0 and b == 0:
        print("YES")
        print(*[i for i in range(1, n + 1)])
        print(*[i for i in range(1, n + 1)])
        continue
    if a >= b:
        if a + b == n:
            print("YES")
            print(*[i for i in range(1, n + 1)])
            print(
                *[i for i in range(n - b + 1, n + 1)] + [i for i in range(1, n - b + 1)]
            )
            continue
        else:
            print("YES")
            print(*[i for i in range(1, n + 1)])
            print(
                *[i for i in range(1, n - (a + b) + 1)]
                + [i for i in range(n - b + 1, n + 1)]
                + [i for i in range(n - (a + b) + 1, n - b + 1)]
            )
            continue
    else:
        if a + b == n:
            print("YES")
            print(
                *[i for i in range(n - a + 1, n + 1)] + [i for i in range(1, n - a + 1)]
            )
            print(*[i for i in range(1, n + 1)])
            continue
        else:
            print("YES")
            print(
                *[i for i in range(1, n - (a + b) + 1)]
                + [i for i in range(n - a + 1, n + 1)]
                + [i for i in range(n - (a + b) + 1, n - a + 1)]
            )
            print(*[i for i in range(1, n + 1)])
            continue
