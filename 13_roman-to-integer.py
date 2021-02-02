class Solution:
    def roman_to_integer(self, s: str) -> int:
        dict = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        int_list = []
        for letter in s:
            int_list.append(dict[letter])

        for index, num in enumerate(int_list):
            if index < len(int_list) - 1:
                num2 = int_list[index + 1]
                if num < num2:
                    int_list[index + 1] = num2 - num
                    int_list[index] = 0

        output = 0
        for value in int_list:
            output += value

        return output

s = Solution()
print(s.roman_to_integer('MCMXLIV'))
