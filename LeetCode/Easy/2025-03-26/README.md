
# 🌟 605. Can Place Flowers

> 📏 **Date:** 2025-03-26  
> 🌟 **Difficulty:** `Easy`  
> 📚 **Category:** LeetCode Solutions  

---

## 📚 Problem Statement  
You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.

Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.

 

Example 1:

Input: flowerbed = [1,0,0,0,1], n = 1
Output: true
Example 2:

Input: flowerbed = [1,0,0,0,1], n = 2
Output: false

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
class Solution:
    def canPlaceFlowers(self, flowerbed, n):
        i = 0
        while i < len(flowerbed):
            if flowerbed[i] == 0:
                left_empty = (i == 0 or flowerbed[i - 1] == 0)
                right_empty = (i == len(flowerbed) - 1 or flowerbed[i + 1] == 0)
                
                if left_empty and right_empty:
                    n -= 1
                    flowerbed[i] = 1  # Plant a flower
                    if n == 0:  # Early exit
                        return True
                    i += 1  # Skip next index since adjacent planting isn't allowed

            i += 1  # Move to next spot
        
        return n <= 0
```

---

### 🚀 Run & Test  
```bash
python 605._Can_Place_Flowers.py
```

---

### 🔗 More Solutions  
📌 [Back to main README](../../README.md)
