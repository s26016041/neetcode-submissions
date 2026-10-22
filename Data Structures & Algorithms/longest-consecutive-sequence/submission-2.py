class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        maxLength = 0 
        
        for num in nums:
            if (num - 1) in numsSet:
                continue
            
            length = 1
            nextNum = num

            while True:
                nextNum+=1

                if nextNum not in numsSet: 
                    break

                length += 1

            if maxLength < length:
                maxLength = length
            
        return maxLength

