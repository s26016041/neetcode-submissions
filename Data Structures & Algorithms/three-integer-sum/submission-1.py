class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        output:List[List[int]] = []
        nums_set = {}
        
        for i, num in enumerate(nums):
            if num not in nums_set:
                nums_set[num] = True
            else:
                continue
            leftNum = i + 1
            rightNum = len(nums) - 1 
            inner_set = {}
            while True:
                if leftNum >= rightNum:
                    break
                if num + nums[leftNum] + nums[rightNum] == 0 :
                    if nums[leftNum] not in inner_set:
                        output.append([num, nums[leftNum], nums[rightNum]])
                        inner_set[nums[leftNum]] = True
                    
                    rightNum-=1
                elif num + nums[leftNum] + nums[rightNum] > 0:
                    rightNum-=1
                elif num + nums[leftNum] + nums[rightNum] < 0:
                    leftNum+=1


        return output


                

