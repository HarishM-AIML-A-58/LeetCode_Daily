
        # 🌟 283. Move Zeroes

> 🗓 **Date:** 2025-03-31  
> 🎯 **Difficulty:** `Easy`  
> 📂 **Category:** LeetCode Solutions  

---

## 📖 Problem Statement  
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

 

Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]

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
    def moveZeroes(self, nums):
        index=0
        for i in range(len(nums)):
            if(nums[i]!=0):
                nums[index],nums[i]=nums[i],nums[index]
                index+=1
```

---

### 🚀 **Run & Test**  
```bash
python 283_Move_Zeroes.py
```

---

### 🔗 **More Solutions**  
📌 [Back to main README](../../README.md)
