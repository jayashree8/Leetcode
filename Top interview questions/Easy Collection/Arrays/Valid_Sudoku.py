'''
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:
A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned.

Input: board = 
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true
'''

''' MY CODE '''
board = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

flag = 0

for i in range(9):
    row = []
    temp = board[i]
    for i in temp:
        if i==".":
            continue
        else:
            row.append(i)
    print(row)
    if sorted(list(set(row))) == sorted(row):
        continue
    else:
        flag==1
        break

trans_mat = [[board[j][i] for j in range(9)] for i in range(9)]
print(trans_mat)

for i in range(9):
    col = []
    temp = trans_mat[i]
    for i in temp:
        if i==".":
            continue
        else:
            col.append(i)
    print(col)
    if sorted(list(set(col))) == sorted(col):
        continue
    else:
        flag==1
        break

