class Solution:
    def intToRoman(self, num: int) -> str:
        dict = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M'
        }
        output = ''
        for i in range(len(str(num)) - 1, -1,  -1):
            current_power = 10 ** i
            count = 0
            while (num - current_power) >= 0:
                num -= current_power
                count += 1
            if count < 5:
                if count == 4:
                    output += dict[current_power] + dict[5 * current_power]
                else:
                    output += count * dict[current_power]
            elif count == 9:
                output += dict[current_power] + dict[10 * current_power]
            else:
                output += dict[5 * current_power] + (count - 5) * dict[current_power]



        return output




s = Solution()
print(s.intToRoman(num=1994))