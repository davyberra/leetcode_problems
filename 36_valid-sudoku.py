class Solution:
    def isValidSudoku(self, board: list) -> bool:
        rows, columns, boxes = [{} for _ in range(9)], [{} for _ in range(9)], [{} for _ in range(9)]
        output = True
        for row, list in enumerate(board):
            for column, value in enumerate(list):
                if value == '.':
                    pass
                else:
                    box = (column // 3) + ((row // 3) * 3)
                    if rows[row].get(value):
                        return False
                    if columns[column].get(value):
                        return False
                    if boxes[box].get(value):
                        return False

                    rows[row][value] = True
                    columns[column][value] = True
                    boxes[box][value] = True

        return output




board = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
    , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
    , [".", "9", "8", ".", ".", ".", ".", "6", "."]
    , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
    , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
    , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
    , [".", "6", ".", ".", ".", ".", "2", "8", "."]
    , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
    , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

s = Solution()
print(s.isValidSudoku(board))
print((8 // 3) + ((8 // 3) * 3))