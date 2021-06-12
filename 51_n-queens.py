class Solution:
    def solveNQueens(self, n):
        def dfs(
                queens: list,
                columns: list,
                row: int,
                d_sum: list,
                d_difference: list
        ):
            # Define case for returning successful value
            p = len(queens)
            if p == n:
                result.append(queens)
                return None
            for column in range(n):
                if column in columns or row + column in d_sum or row - column in d_difference:
                    pass
                else:
                    dfs(
                        queens+[column],
                        columns+[column],
                        row+1,
                        d_sum+[row+column],
                        d_difference+[row-column]
                    )

        result = []
        dfs([], [], 0, [], [])
        output = [['.'*i + 'Q' + '.'* (n - i - 1) for i in sol] for sol in result]


        return output

s = Solution()
print(s.solveNQueens(5))