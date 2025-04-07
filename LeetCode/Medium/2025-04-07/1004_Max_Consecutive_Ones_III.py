class Solution(object):
    def longestOnes(self, nums, k):
        left = 0
        zeroCount = 0
        maxLength = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zeroCount += 1
            
            while zeroCount > k:
                if nums[left] == 0:
                    zeroCount -= 1
                left += 1
            
            maxLength = max(maxLength, right - left + 1)
        
        return maxLength