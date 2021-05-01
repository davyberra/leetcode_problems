class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count, index = 0, len(s) - 1
        output = count
        last_word = False
        while index >= 0:
            if s[index] != ' ':
                last_word = True
                count += 1
            elif s[index] == ' ' and last_word:
                return count
            index -= 1
        return count

s = Solution()
print(s.lengthOfLastWord('d     '))
