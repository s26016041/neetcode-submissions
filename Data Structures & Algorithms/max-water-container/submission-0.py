class Solution:
    def maxArea(self, heights: List[int]) -> int:
        leftHeight = 0
        rightHeight = len(heights) - 1
        maxArea =0 

        while leftHeight != rightHeight:
            area = (rightHeight - leftHeight) * min(heights[leftHeight],heights[rightHeight])
            if area > maxArea:
                maxArea = area

            if heights[leftHeight] > heights[rightHeight]:
                rightHeight -= 1
            elif heights[leftHeight] < heights[rightHeight]:
                leftHeight += 1
            else:
                leftHeight += 1

        return maxArea