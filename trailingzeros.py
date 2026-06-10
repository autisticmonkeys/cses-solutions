n = int(input())
test5 = 5
num5 = 0
while n >= test5:
    num5 += n // test5
    test5 *= 5
print(num5)
