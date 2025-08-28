class Solution(object):
    def areaOfMaxDiagonal(self, dimensions):
        """
        :type dimensions: List[List[int]]
        :rtype: int
        """
    
        max_area = -1
        max_dia = -1

        for l, w in dimensions:

            diagonal = l*l + w*w
            area = l*w

            if diagonal > max_dia or (diagonal == max_dia and area > max_area):
                max_dia = diagonal
                max_area = area
                print(max_area)
        return max_area

if __name__ == "__main__":
    print(Solution().areaOfMaxDiagonal([[9,3],[10,3]]))

