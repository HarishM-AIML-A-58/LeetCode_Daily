
        # 🌟 1004. Max Consecutive Ones III

> 🗓 **Date:** 2025-04-07  
> 🎯 **Difficulty:** `Medium`  
> 📂 **Category:** LeetCode Solutions  

---

## 📖 Problem Statement  
Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

 

Example 1:

Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
Output: 6
Explanation: [1,1,1,0,0,1,1,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
Example 2:

Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
Output: 10
Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

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
```

---

### 🚀 **Run & Test**  
```bash
python 1004_Max_Consecutive_Ones_III.py
```

---

### 🔗 **More Solutions**  
📌 [Back to main README](../../README.md)
