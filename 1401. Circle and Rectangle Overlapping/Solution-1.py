class Solution:
    def checkOverlap(
        self,
        radius: int,
        xCenter: int,
        yCenter: int,
        x1: int,
        y1: int,
        x2: int,
        y2: int,
    ) -> bool:
        # find the closest point of the rectangle to the center of the circle
        closest_x = max(min(xCenter, x2), x1)
        closest_y = max(min(yCenter, y2), y1)

        # distance components from the circle's center to this closest point
        dist_x = xCenter - closest_x
        dist_y = yCenter - closest_y

        # using pythagorean theorem we find the distance but since square roots can get complex we'll let them stay squares only
        return dist_x**2 + dist_y**2 <= radius**2
