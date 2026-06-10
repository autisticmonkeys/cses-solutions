#  this program takes two inputs, one integer and another line of integers, up till the first inputted integer
#  , except for one random number between 1 and that number, and returns that number
n = int(input(""))
arr = list(map(int, input().split()))[:n-1]
whole = n*(n+1)/2
arr_sum = sum(arr)
missing = int(whole - arr_sum)
print(missing)