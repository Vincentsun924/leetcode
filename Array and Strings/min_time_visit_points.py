class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """

        total = 0

        #loop through the points, but we want to stop at the second to last point because we are comparing it with the next point and we get an indexing error if nothhing is next
        for i in range(len(points) - 1):
            # we want to the absolute value because we dont care in what direction
            #this dx is saying to subtract the x value of the current point from the next point, this tells us the horizontle distance, same logic with y
            dx = abs(points[i+1][0] - points[i][0])
            dy = abs(points[i+1][1] - points[i][1])
            # total += max(dx, dy)
            #or 
            #here, the min is how much we can go diagonally before we hit the same x value as the next point and the dx - dy is rest of the distance we need to cover so its gonna be up or down.  
            total += min(dx,dy) + abs(dx - dy)
            
            
            
        return total

                
            