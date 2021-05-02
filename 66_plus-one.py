class Solution:
    def plusOne(self, digits: list) -> list:
        i = len(digits) - 1

        while True:
            if digits[i] == 9:
                if i == 0:
                    digits = [0 for _ in range(len(digits) + 1)]
                    digits[0] = 1
                    return digits

                else:
                    digits[i] = 0
                    i -= 1
            else:
                digits[i] += 1
                return digits


s = Solution()
print(s.plusOne(digits=[9,9,9,]))

tab = [[0] * 7 for i in range(3)]
tab[0] = [1] * 7
print(tab)
