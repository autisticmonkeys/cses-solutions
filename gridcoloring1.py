n, m = map(int, input().split())
grid = [input() for _ in range(n)]
letters = ['A','B','C','D']
'''
if upper row available, check if the letter is present in the square above
if not the beginning of the row, check if the letter is present in the square to the left
choose the letter which is not present in the above and left squares, and in the current square, and assign it to the current square
'''
for i in range(n):
    for j in range(m):
        for ch in letters:
            # check:
            # ch != original
            # ch != above
            # ch != left
            if ch != grid[i][j] and (i == 0 or ch != grid[i-1][j]) and (j == 0 or ch != grid[i][j-1]):
                grid[i] = grid[i][:j] + ch + grid[i][j+1:]
                break
            
for row in grid:
    print(row)