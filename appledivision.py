n = int(input())
weights = list(map(int, input().split()))
# each apple will either go in group one or group two, so we can use a bitmask to represent the groups
# there are 2^n possible ways to divide the apples into two groups
min_diff = float('inf')
for mask in range(1<<n):
    subset_sum = 0
    for i in range(n):
        if mask & (1 << i):
            subset_sum += weights[i]
    other_subset_sum = sum(weights) - subset_sum
    diff = abs(subset_sum - other_subset_sum)
    min_diff = min(min_diff, diff)
print(min_diff)