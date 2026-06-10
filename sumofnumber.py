n = int(input())
i = 1
numlist = []
while n // (10**(i-1)) >= 1:
    temp = n%10**(i-1)
    digit = (n%10**i - temp)//(10**(i-1))
    numlist.append(digit)
    i += 1
print(sum(numlist))