
        # 🌟 1732. Find the Highest Altitude

> 🗓 **Date:** 2025-04-11  
> 🎯 **Difficulty:** `Easy`  
> 📂 **Category:** LeetCode Solutions  

---

## 📖 Problem Statement  
There is a biker going on a road trip. The road trip consists of n + 1 points at different altitudes. The biker starts his trip on point 0 with altitude equal 0.

You are given an integer array gain of length n where gain[i] is the net gain in altitude between points i​​​​​​ and i + 1 for all (0 <= i < n). Return the highest altitude of a point.

 

Example 1:

Input: gain = [-5,1,5,0,-7]
Output: 1
Explanation: The altitudes are [0,-5,-4,1,1,-6]. The highest is 1.
Example 2:

Input: gain = [-4,-3,-2,-1,4,3,2]
Output: 0
Explanation: The altitudes are [0,-4,-7,-9,-10,-6,-3,-1]. The highest is 0.

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
    def largestAltitude(self, gain):
        altitude = 0
        max_altitude = 0
        for g in gain:
            altitude += g
            max_altitude = max(max_altitude, altitude)
        return max_altitude

```

---

### 🚀 **Run & Test**  
```bash
python 1732_Find_the_Highest_Altitude.py
```

---

### 🔗 **More Solutions**  
📌 [Back to main README](../../README.md)
