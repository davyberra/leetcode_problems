class Solution:
    def rotate(self, matrix):
        l = len(matrix) - 1
        hash_map = {}
        for i, row in enumerate(matrix):
            j = 0
            temp = row[:]
            while j <= len(matrix) - 1:

                hash_map[row[j]] = True
                row[j], matrix[j][l] = matrix[l][j], temp[j]
                j += 1
            l -= 1

s = Solution()
matrix = [[1,2,3],[4,5,6],[7,8,9]]
s.rotate(matrix)
print(matrix)