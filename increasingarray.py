# this program returns the minimum number of moves required to turn an array into an increasing array
n = int(input(""))
arr = list(map(int, input().split()))[:n]
i = 0
moves = 0
while i <= n-2:
    if arr[i+1] < arr[i]:
        moves = moves + (arr[i] - arr[i+1])
        arr[i+1] = arr[i]
    i += 1
print(moves)