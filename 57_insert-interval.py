class Solution:
    def insert(self, intervals: list, newInterval: list):
        if len(intervals) == 0:
            return [newInterval]
        inserted = False
        for i, val in enumerate(intervals):
            if val[0] > newInterval[0]:
                intervals.insert(i, newInterval)
                inserted = True
                break
        if not inserted:
            intervals.append(newInterval)

        merged_intervals = [intervals[0]]
        last = 0
        for val in intervals[1:]:
            if merged_intervals[last][1] >= val[0]:
                if merged_intervals[last][1] < val[1]:
                    merged_intervals[last][0], merged_intervals[last][1] = merged_intervals[last][0], val[1]
            else:
                merged_intervals.append(val)
                last += 1

        return merged_intervals

s = Solution()
print(s.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]))