class Solution():
    def setZeroes(self, matrix):
        columns, rows = False, False
        for val in matrix[0]:
            if val == 0:
                rows = True
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                columns = True

        for row_i in range(1, len(matrix)):
            for column_i in range(1, len(matrix[0])):
                if matrix[row_i][column_i] == 0:
                    matrix[0][column_i] = 0
                    matrix[row_i][0] = 0

        for i in range(1, len(matrix[0])):
            if matrix[0][i] == 0:
                for j in range(1, len(matrix)):
                    matrix[j][i] = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] == 0:
                for j in range(1, len(matrix[i])):
                    matrix[i][j] = 0
        if rows:
            for i in range(len(matrix[0])):
                matrix[0][i] = 0
        if columns:
            for i in range(len(matrix)):
                matrix[i][0] = 0

        return matrix

s = Solution()
print(s.setZeroes([[1,2,3,4],[5,0,7,8],[0,10,11,12],[13,14,15,0]]
))