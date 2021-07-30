class Solution:
    def solve(self, board: list):
        m, n = len(board), len(board[0])
        q = []
        for j in range(n):
            q.append([0, j])
        for i in range(1, m - 1):
            q.append([i, 0])
            q.append([i, n-1])
        for j in range(n):
            q.append([m - 1, j])

        while len(q) > 0:
            i, j = q.pop()
            if 0 <= i < m and 0 <= j < n and board[i][j] == 'O':
                board[i][j] = 'S'
                q.append([i, j-1])
                q.append([i, j+1])
                q.append([i-1, j])
                q.append([i+1, j])

        for i in range(m):
            for j in range(n):
                if board[i][j] != 'S':
                    board[i][j] = 'X'
                else:
                    board[i][j] = 'O'

        return board


s = Solution()
print(s.solve([["X","O","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]))
