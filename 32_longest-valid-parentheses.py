class Solution:
    def longestValidParentheses(self, s: str) -> int:
        output = 0
        parens = {
            '(': 1,
            ')': -1
        }
        lowest_sum = 0
        lowest_sum_changed = False
        i = 0
        done = False
        if s:
            while not done:
                if s[i] == ')':
                    pass
                else:
                    count = 1
                    cur_sum = 1
                    for j in s[i + 1:]:
                        count += 1
                        cur_sum += parens[j]
                        lowest_sum = min(lowest_sum, cur_sum)
                        if j == ')' and not lowest_sum_changed:
                            lowest_sum = cur_sum
                            lowest_sum_changed = True
                        if cur_sum < 0:
                            break
                        elif cur_sum == 0 and count > output and j == ')':
                            output = count
                    if not lowest_sum_changed:
                        return output
                if lowest_sum > 1:
                    i += lowest_sum
                else:
                    i += 1
                if i >= len(s):
                    done = True

        return output

s1 = ")()())"
s = Solution()
print(s.longestValidParentheses(s1))
