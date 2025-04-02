
        # 🌟 11.Container With Most Water

> 🗓 **Date:** 2025-04-02  
> 🎯 **Difficulty:** `Medium`  
> 📂 **Category:** LeetCode Solutions  

---

## 📖 Problem Statement  
ou are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

 

Example 1:


Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.
Example 2:

Input: height = [1,1]
Output: 1

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
    def maxArea(self, height):
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            width = right - left
            min_height = min(height[left], height[right])
            max_area = max(max_area, width * min_height)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
```

---

### 🚀 **Run & Test**  
```bash
python 11Container_With_Most_Water.py
```

---

### 🔗 **More Solutions**  
📌 [Back to main README](../../README.md)
