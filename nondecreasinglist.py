import sys

n = int(input())
arr = list(map(int, input().split()))[:n]
i = 0
count = 0
while i <= n - 2:
    if arr[i] > arr[i + 1]:
        count += 1
        if count > 1:
            print("NO")
            sys.exit()

        if i > 0 and arr[i - 1] > arr[i + 1]:
            arr[i + 1] = arr[i]
        else:
            arr[i] = arr[i + 1]
    i += 1
print("YES")
