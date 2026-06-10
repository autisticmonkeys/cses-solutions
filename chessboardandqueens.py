board = []
for _ in range(8):
    board.append(input())
cols = set() #to keep track of which columns are occupied by queens
diag = set() #to keep track of which diagonals are occupied by queens
anti_diag = set() #to keep track of which anti-diagonals are occupied by queens
def solve(row):
    if row == 8:
        return 1 #since we're at the last row, we found a valid solution, so we can count it and return
    count = 0 #starting from 0, we will add to this count every time we find a valid solution
    for col in range(8): #for each row, we are cycling through all the columns
        if board[row][col] == '*':
            continue #if the square is reserved, we skip it
        if col in cols:
            continue #if there is a queen in the same column, we skip it
        if (row - col) in diag:
            continue #if there is a queen in the same diagonal, we skip it
        if (row + col) in anti_diag:
            continue #if there is a queen in the same anti-diagonal, we skip it
        #if we get here, it means that the square is not reserved and there are no queens in the same column, diagonal, or anti-diagonal, so we can place a queen here
        cols.add(col) #we add the column to the set of occupied columns
        diag.add(row - col) #we add the diagonal to the set of occupied diagonals
        anti_diag.add(row + col) #we add the anti-diagonal to the set of occupied anti-diagonals
        count += solve(row + 1) #we recurse the function for the next row, and add the number of solutions found to our count
        cols.remove(col) #after we finish recursing, we remove the column from the set of occupied columns
        diag.remove(row - col) #we remove the diagonal from the set of occupied diagonals
        anti_diag.remove(row + col) #we remove the anti-diagonal from the set of occupied anti-diagonals
    return count #after we finish cycling through all the columns, we return the count of solutions found
print(solve(0)) #we start the recursion from the first row, and print the total number of solutions found
