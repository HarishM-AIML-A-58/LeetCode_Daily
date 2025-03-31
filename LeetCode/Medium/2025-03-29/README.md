
# 🌟 Increasing Triplet Subsequence

> 📏 **Date:** 2025-03-29  
> 🌟 **Difficulty:** `Medium`  
> 📚 **Category:** LeetCode Solutions  

---

## 📚 Problem Statement  
Given an integer array nums, return true if there exists a triple of indices (i, j, k) such that i < j < k and nums[i] < nums[j] < nums[k]. If no such indices exists, return false.

 

Example 1:

Input: nums = [1,2,3,4,5]
Output: true
Explanation: Any triplet where i < j < k is valid.
Example 2:

Input: nums = [5,4,3,2,1]
Output: false
Explanation: No triplet exists.
Example 3:

Input: nums = [2,1,5,0,4,6]
Output: true
Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

---

## 💪 Solution Approach  
🔹 **Key Concepts Used:**  
- Explain briefly what approach was used to solve the problem.

🔹 **Complexity Analysis:**  
- 🫠 **Time Complexity:** O(...)  
- 📂 **Space Complexity:** O(...)  

---

## 🖥️ Solution Code  
```python
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
```

---

### 🚀 Run & Test  
```bash
python Increasing_Triplet_Subsequence.py
```

---

### 🔗 More Solutions  
📌 [Back to main README](../../../README.md)
