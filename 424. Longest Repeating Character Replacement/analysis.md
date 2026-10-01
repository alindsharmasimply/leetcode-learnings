## 1. The Core Concept (What is this?)
    Another sliding window problem but a little tricky.

## 2. Architectural Trade-offs
* **Approach A:** Maintain the `max_length` as well as the `max_frequency` at every point during the traversal. Keep storing the frequency of every character in the dictionary but also maintain the max freq of a character within the window. After that just ensure that the window's length - max_freq is always <= k. If it's not then we have to increment the left pointer too as well as reduce its character's count from the dictionary too.
* **Approach B:** 

## 3. Insights
* **Insight A:** Time Complexity: O(n) and Space Complexity: O(26)
* **Insight B:** 

## 4. The Pitfall Log
* **Gotcha 1:** 
* **Gotcha 2:** 

## 5. Deep-Dive References
* 