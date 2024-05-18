"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4
 

Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""
class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        
        res = 0
        for p1 in points:
            angles = {}
            max = 0
            same_points = 0
            for p2 in points:
                if p1 == p2:
                    same_points += 1
                    continue

                if p1[0] == p2[0]:
                    angle = float("inf")
                else:
                    angle = (p1[1] - p2[1]) / (p1[0] - p2[0])
                angles[angle] = angles.get(angle, 0) + 1
                if max < angles[angle]:
                    max = angles[angle]
            if res < max + same_points:
                res = max + same_points

        return res