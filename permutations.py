# this program prints number from 1 to n in a way such that the difference of any two adjacent numbers isn't 1
n = int(input())
if n == 1:
    print(1)
elif n<=3:
    print("NO SOLUTION")
else:
    evens = range(2, n+1, 2)
    odds = range(1, n+1, 2)
    print(*evens,*odds)