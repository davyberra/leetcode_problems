def strStr(haystack: str, needle: str) -> int:
    if len(haystack) == 0:
        return 0
    else:
        output = -1
        span = len(needle)
        for i in range(len(haystack) - span + 1):
            if haystack[i:i + span] == needle:
                output = i
                break

        return output



print(strStr('heellooll', 'll'))