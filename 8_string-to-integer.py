class Solution:
    def myAtoi(self, s: str) -> int:
        s_list = []
        finished_leading_zeroes = False
        for value in s:
            if value == ' ':
                continue
            elif value == '0':
                if finished_leading_zeroes == False:
                    continue
                else:
                    s_list.append(value)
            elif value == '-' or value == '+':
                s_list.append(value)
            elif s[s.index(value):].isnumeric():
                finished_leading_zeroes = True
                s_list.append(value)

        output = ''
        for value in s_list:
            output += value
        output = int(output)
        if output > 2 ^ 32:
            output = 2 ^ 32
        elif output < -2 ^ 32:
            output = -2 ^ 32
        return output

s = Solution()
print(s.myAtoi('  -003010'))