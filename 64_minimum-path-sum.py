class Solution:
    def minPathSum(self, grid: list):
        sum_grid = [[0 for i in grid[0]] for j in grid]
        sum_grid[0][0] = grid[0][0]
        for column in range(1, len(grid[0])):
            sum_grid[0][column] = sum_grid[0][column - 1] + grid[0][column]
        for row in range(1, len(grid)):
            sum_grid[row][0] = sum_grid[row - 1][0] + grid[row][0]
        for row in range(1, len(grid)):
            for column in range(1, len(grid[row])):
                sum_grid[row][column] = min(sum_grid[row - 1][column], sum_grid[row][column - 1]) + grid[row][column]

        return sum_grid[-1][-1]


s = Solution()
print(s.minPathSum([[1,3,1],[1,5,1],[4,2,1],[1,5,3],[7,8,4],[4,3,7],[9,8,10],[1,1,3],[2,5,1]]))