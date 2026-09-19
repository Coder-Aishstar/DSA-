class Solution(object):
    def checkOverlap(self, radius, xcenter, ycenter, x1, y1, x2, y2):
        closestx = max(x1, min(xcenter, x2))
        closesty = max(y1, min(ycenter, y2))
        dx = xcenter - closestx
        dy = ycenter - closesty
        return dx*dx + dy*dy <= radius*radius

        """
        :type radius: int
        :type xCenter: int
        :type yCenter: int
        :type x1: int
        :type y1: int
        :type x2: int
        :type y2: int
        :rtype: bool
        """
        