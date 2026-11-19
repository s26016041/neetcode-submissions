class Solution:
    def trap(self, height: List[int]) -> int:
        leftIndex = 0
        rightIndex = len(height) - 1
        leftMax = height[leftIndex]
        rightMax = height[rightIndex]
        output = 0

        while leftIndex < rightIndex:
            if leftMax < rightMax:
                leftIndex +=1
                leftMax = max(leftMax, height[leftIndex])
                output += leftMax - height[leftIndex]
            else:
                rightIndex-=1
                rightMax = max(rightMax, height[rightIndex])
                output += rightMax - height[rightIndex]
            
        return output
            