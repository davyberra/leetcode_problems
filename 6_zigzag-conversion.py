class Solution:
    def convert(self, s: str, numRows: int) -> str:
        array = [[] for _ in range(numRows)]
        output = ''
        x = 0
        dir = 1
        for i in range(len(s)):
            array[x].append(s[i])
            x += dir
            if x == 0 or x == (numRows - 1):
                dir = -dir
        for list in array:
            for letter in list:
                output += letter
        return output





s = Solution()
print(s.convert('PAYPALISHIRING', 4))