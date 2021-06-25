class Solution:
    def numDecodings(self, s: str) -> int:
        if s[0] == '0':
            return 0
        i, total = 0, 0
        done = False
        while not done:
            if i <= 1 and s[i] != '0':
                total += 1
                i += 1
            else:
                if i < len(s) - 1:
                    if s[i + 1] == '0':
                        total += 1
                        i += 2
                if i > 0:
                    if s[i - 1] == '1' or s[i - 1] == '2' and int(s[i]) <= 6:
                        total += 1
                        i += 1
                    else:
                        i += 1
            if i >= len(s) - 1:
                done = True

        return total

s = Solution()
print(s.numDecodings('22'))