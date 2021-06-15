class Solution:
    def merge(self, intervals: list):
        right = len(intervals) - 1
        while right > 0:
            count = 0
            left = 0
            while left < right:
                if len(intervals[left]) > 0 and len(intervals[right]) > 0:
                    if intervals[left][0] >= intervals[right][0]:
                        a, b = right, left
                    else:
                        a, b = left, right
                    if intervals[a][1] >= intervals[b][0]:
                        if intervals[a][1] <= intervals[b][1]:
                            intervals[left][0], intervals[left][1] = intervals[a][0], intervals[b][1]
                            count += 1
                            intervals[right] = []
                        else:
                            intervals[left][0], intervals[left][1] = intervals[a][0], intervals[a][1]
                            intervals[right] = []
                left += 1

            right -= 1

        for i in range(len(intervals) - 1, -1, -1):
            if len(intervals[i]) == 0:
                intervals.remove(intervals[i])

        return intervals


s = Solution()
print(s.merge([[1,4],[0,5]]))
