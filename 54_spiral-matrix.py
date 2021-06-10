class Solution:
    def spiralOrder(self, matrix: list) -> list:
        row_count, column_count = len(matrix), len(matrix[0])
        counting_columns = True
        count = 0
        dx_x, dx_y = 1, 1
        i, j = 0, 0
        output = []
        hashmap = {}
        while True:
            if count >= row_count * column_count:
                return output
            if (i, j) in hashmap or i >= row_count or i < 0 or j >= column_count or j < 0:
                if counting_columns:
                    j -= dx_x
                    i += dx_y
                    dx_x = -dx_x

                elif not counting_columns:
                    i -= dx_y
                    j += dx_x
                    dx_y = -dx_y
                counting_columns = not counting_columns
            else:
                hashmap[i, j] = True
                output.append(matrix[i][j])
                if counting_columns:
                    j += dx_x
                elif not counting_columns:
                    i += dx_y

                count += 1



s = Solution()
print(s.spiralOrder([[1,2,3,4],[5,6,7,8],[9,10,11,12]]))
