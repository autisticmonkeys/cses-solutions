n = int(input())
i = 1
while i <= n:
    total = (i**2) * ((i**2) - 1) // 2
    attack = 4 * (i - 1) * (i - 2)
    print(total - attack)
    i += 1
