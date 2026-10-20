class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:        
        numsLen = len(nums)
        output = [1] * numsLen

        initialNnumber = 1
        for i in range(numsLen):
            output[i] = initialNnumber
            initialNnumber *= nums[i]

        initialNnumber = 1
        for i in range(numsLen- 1, -1, -1):
            output[i] *= initialNnumber
            initialNnumber *= nums[i]

        return output
