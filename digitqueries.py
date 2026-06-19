q = int(input())
for _ in range(q):
    k = int(input())
    n = 1
    while k - 9*(10**(n-1))*n > 0:
        k -= 9*(10**(n-1))*n
        n += 1
    add = (k - 1) // n
    num_add = 10**(n-1) + add
    val = (k-1) % n
    print(str(num_add)[val])