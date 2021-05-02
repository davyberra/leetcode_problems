class Solution:
    def balancedStringSplit(self, s: str) -> int:
        output = 0
        cur_sum = 0
        d = {
            'R': 1,
            'L': -1
        }
        for i, val in enumerate(s):
            cur_sum += d[val]
            if cur_sum == 0:
                output += 1

        return output

s = Solution()
print(s.balancedStringSplit("LRRLRLRRLRLL"))