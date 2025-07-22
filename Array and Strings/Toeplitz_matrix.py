class Solution(object):
    def isToeplitzMatrix(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        """
        #len of matrix is 3 bc 3 rows
        for i in range(1, len(matrix)):
            #len of matric [0] is 4 because 4 columns
            for j in range(1, len(matrix[0])):
                if matrix[i][j] != matrix[i-1][j-1]:
                    return False
        return True
        