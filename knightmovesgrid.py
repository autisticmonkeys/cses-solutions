from collections import deque

n = int(input())
moves = [(2, 1), (1, 2), (-1, 2), (-2, 1), (-2, -1), (-1, -2), (1, -2), (2, -1)]
grid = [[-1] * n for _ in range(n)]
grid[0][0] = 0
queue = deque([(0, 0)])
while queue:
    x, y = queue.popleft()
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[nx][ny] == -1:
            grid[nx][ny] = grid[x][y] + 1
            queue.append((nx, ny))
for row in grid:
    print(*row)
