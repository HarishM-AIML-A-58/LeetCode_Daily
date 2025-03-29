class Solution(object):
    def increasingTriplet(self, nums):
        first = float('inf')
        second = float('inf')
        
        for num in nums:
            if num <= first:
                first = num  
            elif num <= second:
                second = num  
            else:
                
                return True
        
        return False