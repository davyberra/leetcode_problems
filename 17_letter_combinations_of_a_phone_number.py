class Solution:
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

    def get_new_comb(self, digits: str, comb: str, i, output: list):
        for letter in self.phone_dict[digits[i]]:
            current_comb = comb
            current_comb += letter
            if i + 1 != len(digits):
                self.get_new_comb(digits, current_comb, i + 1, output)
            else:
                output.append(current_comb)

        return output

    def letterCombinations(self, digits: str) -> list:
        output = []
        if len(digits) < 1:
            return output
        else:

            output = self.get_new_comb(digits, '', 0, output)

            return output


        # for letter1 in phone_dict[digits[0]]:
        #     for letter2 in phone_dict[digits[1]]:
        #         comb = letter1 + letter2
        #         output.append(comb)
        #
        # return output


s = Solution()
print(s.letterCombinations('23489'))
