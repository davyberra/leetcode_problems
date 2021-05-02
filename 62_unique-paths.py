class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        table = [[0] * n for _ in range(m)]

        table[0] = [1] * n

        for i in range(m):
            table[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                table[i][j] = table[i - 1][j] + table[i][j - 1]

        return (table[-1][-1], table)


s = Solution()
print(s.uniquePaths(4,7))