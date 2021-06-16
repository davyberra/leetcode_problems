class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = {}
        arr = []
        least = None
        if len(t) > len(s):
            return ""
        for i, char in enumerate(s):
            if char in t:
                if char in d and len(arr) == len(t):
                    arr.remove(d[char])
                d[char] = i
                arr.append(i)

                if len(arr) == len(t) and len(d) == len(t):

                    cur = [arr[-1], arr[0]]
                    if not least:
                        least = [arr[-1], arr[0]]
                    elif least[0] - least[1] > cur[0] - cur[1]:
                        least = cur


        if not least:
            return ""
        else:
            return s[least[1]:least[0] + 1]

s = Solution()
print(s.minWindow('bba', 'ab'))
print(s.minWindow("ADOBECODEBANC", "ABC"))
print(s.minWindow('abecabc', 'abc'))
