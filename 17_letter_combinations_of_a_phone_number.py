class Solution:
    def letterCombinations(self, digits: str) -> list:
        phone_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        output = []
        for letter1 in phone_dict[digits[0]]:
            for letter2 in phone_dict[digits[1]]:
                comb = letter1 + letter2
                output.append(comb)

        return output


s = Solution()
print(s.letterCombinations('23'))
