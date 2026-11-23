class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda x: x[1])

        arrows = 1
        arrow_x = points[0][1]

        for i in range(1, len(points)):
            start, end = points[i]
            if start > arrow_x:
                arrows += 1
                arrow_x = end

        return arrows