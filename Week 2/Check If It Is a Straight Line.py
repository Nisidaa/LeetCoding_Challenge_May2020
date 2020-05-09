# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
# Check if these points make a straight line in the XY plane.
# Example 1:
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
# Example 2:
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false
# Constraints:
# 2 <= coordinates.length <= 1000
# coordinates[i].length == 2
# -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
# coordinates contains no duplicate point.

class Solution:
    def checkStraightLine(self, coordinates: list) -> bool:
        for point in range(2, len(coordinates)):
            if not self.expression(coordinates[0], coordinates[1], coordinates[point]):
                return False
        return True

    def expression(self, point1: list, point2: list, point: list) -> int:
        right = (point[0]-point1[0])*(point2[1]-point1[1])
        left = (point[1]-point1[1])*(point2[0]-point1[0])
        return left == right


print(Solution().checkStraightLine([[-7,-3],[-7,-1],[-2,-2],[0,-8],[2,-2],[5,-6],[5,-5],[1,7]]))
