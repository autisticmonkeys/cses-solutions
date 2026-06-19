dirs = [(-1, 0), (1, 0), (0, 1), (0, -1)]
conv = {"U": 0, "D": 1, "R": 2, "L": 3, "?": 4}
path = [conv[ch] for ch in input()]

visited = [[True] * 9 for _ in range(9)]
for i in range(1, 8):
    for j in range(1, 8):
        visited[i][j] = False


def solve(x, y, step):
    if step == 48 and (x, y) == (7, 1):
        return 1 
    if (step == 48 and (x, y) != (7, 1)) or ((x, y) == (7, 1)):
        return 0
    visited[x][y] = True
    u = visited[x - 1][y]
    d = visited[x + 1][y]
    l = visited[x][y - 1]
    r = visited[x][y + 1] 
    move = path[step]  
    # split pruning
    if u and d and not l and not r:
        visited[x][y] = False
        return 0
    if l and r and not u and not d:
        visited[x][y] = False
        return 0
    count = 0
    # input path
    if move < 4:
        dx, dy = dirs[move]
        nx = x + dx
        ny = y + dy
        if not visited[nx][ny]:
            count += solve(nx, ny, step + 1)
    else:
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if not visited[nx][ny]:
                count += solve(nx, ny, step + 1)
    visited[x][y] = False
    return count
print(solve(1, 1, 0))