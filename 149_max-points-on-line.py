class Solution:
    def maxPoints(self, points: list) -> int:
        if len(points) == 1 or len(points) == 2:
            return len(points)
        most_points = 2
        for i in range(len(points)):
            for j in range(i + 1, len(points)):
                dx, dy = points[j][0] - points[i][0], points[j][1] - points[i][1]
                count = 2
                for k in range(j + 1, len(points)):
                    if dx != 0 and dy != 0:
                        if (points[k][0] - points[i][0]) / dx == (points[k][1] - points[i][1]) / dy:
                            count += 1
                    elif dx == 0 and points[k][0] == points[i][0] or dy == 0 and points[k][1] == points[i][1]:
                        count += 1
                if count > most_points:
                    most_points = count

        return most_points

s = Solution()
print(s.maxPoints([[-9,-651],[-4,-4],[-8,-582],[9,591],[-3,3]]))