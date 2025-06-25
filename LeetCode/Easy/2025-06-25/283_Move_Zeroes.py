class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        i=0
        n=len(nums)
        for _ in range(n):
            if nums[i]==0:
                nums.pop(i)
                nums.append(0)
            else:
                i+=1
        return nums