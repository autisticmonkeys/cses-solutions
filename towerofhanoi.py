n = int(input())
print(2**n - 1)
def hanoi(n, src, tgt, aux):
    if n == 0:
        return
    hanoi(n -1, src, aux, tgt)
    print(src, tgt)
    hanoi(n -1, aux, tgt, src)
hanoi(n, 1, 3, 2)