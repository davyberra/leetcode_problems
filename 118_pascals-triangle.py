class Solution:
    def generate(self, numRows: int) -> list:
        output = []
        for i in range(numRows):
            row = [0 for _ in range(i + 1)]
            output.append(row)
            if i == 0:
                row[0] = 1
            else:
                row[0], row[-1] = 1, 1
                if i > 1:
                    for j in range(1, i):
                        row[j] = output[i - 1][j - 1] + output[i - 1][j]

        return output

s = Solution()
print(s.generate(30))
