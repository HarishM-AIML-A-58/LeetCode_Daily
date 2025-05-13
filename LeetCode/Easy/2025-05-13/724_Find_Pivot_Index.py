class Solution:
    def pivotIndex(self, nums):
        totalSum = sum(nums)  
        leftSum = 0  
        
        for i in range(len(nums)):
            
            rightSum = totalSum - leftSum - nums[i]
            
           
            if leftSum == rightSum:
                return i  
            
            leftSum += nums[i]
        
        return -1  