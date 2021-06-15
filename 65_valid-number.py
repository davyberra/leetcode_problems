import re

class Solution:
    def valid(self, s: str) -> bool:
        p_dec = re.compile('^[\+\-]?\d*\.?\d*$')
        p_int = re.compile('^[\+\-]?\d*$')
        p_contains_number = re.compile('\d+')

        s_lower = s.lower()
        if s_lower == 'e':
            return False
        if re.search(p_contains_number, s_lower) is None:
            return False
        if 'e' in s_lower:
            s_split = s_lower.split('e')
            if len(s_split) > 2:
                return False
            if re.search(p_contains_number, s_split[0]) is None or re.search(p_contains_number, s_split[1]) is None:
                return False
            res1, res2 = re.search(p_dec, s_split[0]), re.search(p_int, s_split[1])
            return res1 is not None and res2 is not None
        else:
            res1, res2 = re.search(p_dec, s), re.search(p_int, s)
            return res1 is not None or res2 is not None

s = Solution()
print(s.valid('e9'))
print(s.valid('-90E+3'))
print(s.valid('0333.78'))