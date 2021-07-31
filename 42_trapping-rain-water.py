class Solution:
    def trap(self, height: list) -> int:
        left = 0
        arr = [0 for _ in range(len(height))]
        result = 0
        if len(height) < 3:
            return result

        for i, val in enumerate(height):
            if val > left:
                left = val
            elif val < left:
                arr[i] = left - val

        right = 0
        for i, val in reversed(list(enumerate(height))):
            if val >= right:
                right = val
                arr[i] = 0
            elif val < right:
                arr[i] = min((right - val), arr[i])

        result = sum(arr)
        return result

s = Solution()
print(s.trap([0,1,0,2,1,0,1,3,2,1,2,1]))
print(s.trap([4,2,0,3,2,5]))
