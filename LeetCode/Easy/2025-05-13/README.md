
        # 🌟 724. Find Pivot Index

> 🗓 **Date:** 2025-05-13  
> 🎯 **Difficulty:** `Easy`  
> 📂 **Category:** LeetCode Solutions  

---

## 📖 Problem Statement  
Given an array of integers nums, calculate the pivot index of this array.

The pivot index is the index where the sum of all the numbers strictly to the left of the index is equal to the sum of all the numbers strictly to the index's right.

If the index is on the left edge of the array, then the left sum is 0 because there are no elements to the left. This also applies to the right edge of the array.

Return the leftmost pivot index. If no such index exists, return -1.

 

Example 1:

Input: nums = [1,7,3,6,5,6]
Output: 3
Explanation:
The pivot index is 3.
Left sum = nums[0] + nums[1] + nums[2] = 1 + 7 + 3 = 11
Right sum = nums[4] + nums[5] = 5 + 6 = 11
Example 2:

Input: nums = [1,2,3]
Output: -1
Explanation:
There is no index that satisfies the conditions in the problem statement.
Example 3:

Input: nums = [2,1,-1]
Output: 0
Explanation:
The pivot index is 0.
Left sum = 0 (no elements to the left of index 0)
Right sum = nums[1] + nums[2] = 1 + -1 = 0

---

## 💡 Solution Approach  
🔹 **Key Concepts Used:**  
- Explain briefly what approach was used to solve the problem.

🔹 **Complexity Analysis:**  
- 🕑 **Time Complexity:** O(...)  
- 💾 **Space Complexity:** O(...)  

---

## 🖥️ Solution Code  
```python
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
```

---

### 🚀 **Run & Test**  
```bash
python 724_Find_Pivot_Index.py
```

---

### 🔗 **More Solutions**  
📌 [Back to main README](../../README.md)
