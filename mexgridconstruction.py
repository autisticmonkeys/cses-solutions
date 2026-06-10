n = int(input())
'''
to create a grid of size n x n, where each number is the smallest non-negative number
but it cannot appear to its left or above it
'''
def grid(n):
    grid = [[0] * n for _ in range(n)]  
    for i in range(n):
        for j in range(n):
            left = set()
            above = set()
            if j > 0:
                left = set(grid[i][:j])
            if i > 0:
                above = set(grid[k][j] for k in range(i))
            grid[i][j] = 0
            while grid[i][j] in left or grid[i][j] in above:
                grid[i][j] += 1
    return grid   
g = grid(n)
for row in g:
    print(*row)