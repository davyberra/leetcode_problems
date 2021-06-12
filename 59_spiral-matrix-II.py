class Solution:
    def spiralOrder(self, n: int) -> list:
        counting_columns = True
        count = 1
        dx_x, dx_y = 1, 1
        i, j = 0, 0
        output = [[0 for column in range(n)] for row in range(n)]
        hashmap = {}
        while True:
            if count > n ** 2:
                return output
            if (i, j) in hashmap or i >= n or i < 0 or j >= n or j < 0:
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
                output[i][j] = count
                if counting_columns:
                    j += dx_x
                elif not counting_columns:
                    i += dx_y

                count += 1

s = Solution()
print(s.spiralOrder(4))